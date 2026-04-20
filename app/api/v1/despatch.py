from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
import io
import json

from app.core.order_parser import parse_ubl_order
from app.core.ubl_generator import generate_despatch_advice
from app.models.user_models import User, Despatch
from app.data.db import get_db
from app.core.auth import get_current_user

router = APIRouter(tags=["Despatch Advice (v3)"])


# Generates an XML despatch advice file from a XML Order and returns a download to the generated file

@router.post("/generate", status_code=201)
async def generate_despatch(
    order_xml: UploadFile = File(...),
    carrier: str = Form(""),
    dispatch_date: str = Form(""),
    notes: str = Form(""),
    partial_lines: str = Form(""),   # optional JSON string: {"line_id": dispatched_qty, ...}
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    # --- Read uploaded file ---
    xml_bytes = await order_xml.read()
    if not xml_bytes:
        raise HTTPException(status_code=400, detail="Empty uploaded file")

    # --- Parse XML ---
    try:
        order_data = parse_ubl_order(xml_bytes.decode("utf-8"))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # --- Parse partial_lines if provided ---
    parsed_partial = None
    if partial_lines and partial_lines.strip():
        try:
            parsed_partial = json.loads(partial_lines)
        except json.JSONDecodeError:
            raise HTTPException(status_code=422, detail="partial_lines must be valid JSON")

        # Validate: dispatched qty must not exceed ordered qty for each line
        ordered_map = {line["id"]: float(line["quantity"] or 0) for line in order_data["order_lines"]}
        for line_id, qty in parsed_partial.items():
            try:
                qty_float = float(qty)
            except (TypeError, ValueError):
                raise HTTPException(status_code=422, detail=f"Invalid quantity for line {line_id}")
            if qty_float < 0:
                raise HTTPException(status_code=422, detail=f"Dispatched quantity cannot be negative (line {line_id})")
            if line_id in ordered_map and qty_float > ordered_map[line_id]:
                raise HTTPException(
                    status_code=422,
                    detail=f"Dispatched quantity ({qty_float}) exceeds ordered quantity ({ordered_map[line_id]}) for line {line_id}"
                )

    # --- Generate ---
    try:
        xml_content = generate_despatch_advice(
            order_data,
            carrier,
            dispatch_date,
            notes,
            partial_lines=parsed_partial,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # --- Store ---
    doc_uuid = str(uuid4())

    despatch = Despatch(
        uuid=doc_uuid,
        despatch_id=order_data["order_id"],
        xml_content=xml_content,
        source_order_xml=xml_bytes.decode("utf-8"),   # store for edit flow
        user_id=user.id
    )

    db.add(despatch)
    db.commit()

    filename = f"Despatch_{order_data['order_id']}_{doc_uuid}.xml"

    return StreamingResponse(
        io.BytesIO(xml_content.encode("utf-8")),
        media_type="application/xml",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Despatch-UUID": doc_uuid,
        }
    )

# Returns list of all of a user's generated XML documents
@router.get("/list")
def list_despatch_advice(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatches = db.query(Despatch).filter(Despatch.user_id == user.id).all()

    return [
        {
            "uuid": d.uuid,
            "despatch_id": d.despatch_id,
        }
        for d in despatches
    ]

# Returns list of all generated XML documents (admin only)
@router.get("/admin/list")
def list_all_despatch_advice(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    despatches = db.query(Despatch).all()

    return [
        {
            "uuid": d.uuid,
            "despatch_id": d.despatch_id,
            "user_id": d.user_id,
        }
        for d in despatches
    ]


# Retrieve a Despatch Advice document using its ID


@router.get("/id/{id}")
def get_despatch_advice_by_id(
    id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.despatch_id == id).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    return Response(
        content=despatch.xml_content,
        media_type="application/xml",
        headers={
            "Despatch-ID": despatch.despatch_id,
            "Despatch-UUID": despatch.uuid
        }
    )


# Retrieve a Despatch Advice document using its UUID
@router.get("/uuid/{uuid}")
def get_despatch_advice_by_uuid(
    uuid: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.uuid == uuid).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    return Response(
        content=despatch.xml_content,
        media_type="application/xml",
        headers={
            "Despatch-ID": despatch.despatch_id,
            "Despatch-UUID": despatch.uuid
        }
    )


# Download the XML file for a Despatch Advice using its ID
@router.get("/id/download/{id}")
def download_despatch_advice_by_id(
    id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.despatch_id == id).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    filename = f"Despatch_{id}.xml"

    return StreamingResponse(
        io.BytesIO(despatch.xml_content.encode("utf-8")),
        media_type="application/xml",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


# Download the XML file for a Despatch Advice using its UUID
@router.get("/uuid/download/{uuid}")
def download_despatch_advice_by_uuid(
    uuid: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.uuid == uuid).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    filename = f"Despatch_{uuid}.xml"

    return StreamingResponse(
        io.BytesIO(despatch.xml_content.encode("utf-8")),
        media_type="application/xml",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


# Delete a Despatch Advice document using its ID
@router.delete("/id/{id}")
def delete_despatch_advice_by_id(
    id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.despatch_id == id).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    db.delete(despatch)
    db.commit()

    return {"message": "Deleted successfully"}


# Delete a Despatch Advice document using its UUID
def delete_despatch_advice_by_uuid(
    uuid: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.uuid == uuid).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    db.delete(despatch)
    db.commit()

    return {"message": "Deleted successfully"}


# ── Edit flow ────────────────────────────────────────────────

# Returns the original Order XML that was uploaded when this despatch was created.
# Used by the frontend to repopulate the edit form with the original line items.
@router.get("/id/{id}/source-order")
def get_source_order(
    id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.despatch_id == id).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    if not despatch.source_order_xml:
        raise HTTPException(404, "No source order XML stored for this despatch")

    return Response(
        content=despatch.source_order_xml,
        media_type="application/xml",
        headers={"Despatch-ID": despatch.despatch_id, "Despatch-UUID": despatch.uuid}
    )


# Regenerates an existing despatch with updated inputs.
# The UUID and despatch_id are preserved; xml_content is replaced.
# Accepts same multipart form-data as /generate, with an optional new Order XML file.
# If no new file is uploaded, the stored source_order_xml is re-used.
@router.put("/id/{id}/edit")
async def edit_despatch(
    id: str,
    order_xml: UploadFile = File(None),   # optional - re-use stored order if not provided
    carrier: str = Form(""),
    dispatch_date: str = Form(""),
    notes: str = Form(""),
    partial_lines: str = Form(""),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    despatch = db.query(Despatch).filter(Despatch.despatch_id == id).first()

    if not despatch:
        raise HTTPException(404, "Not found")

    if despatch.user_id != user.id and not user.is_admin:
        raise HTTPException(403, "Not allowed")

    # --- Resolve order XML ---
    if order_xml and order_xml.filename:
        xml_bytes = await order_xml.read()
        if not xml_bytes:
            raise HTTPException(status_code=400, detail="Empty uploaded file")
        order_xml_str = xml_bytes.decode("utf-8")
    elif despatch.source_order_xml:
        order_xml_str = despatch.source_order_xml
    else:
        raise HTTPException(
            status_code=422,
            detail="No Order XML provided and no source order stored - please upload the original Order XML"
        )

    # --- Parse XML ---
    try:
        order_data = parse_ubl_order(order_xml_str)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # --- Parse partial_lines if provided ---
    parsed_partial = None
    if partial_lines and partial_lines.strip():
        try:
            parsed_partial = json.loads(partial_lines)
        except json.JSONDecodeError:
            raise HTTPException(status_code=422, detail="partial_lines must be valid JSON")

        ordered_map = {line["id"]: float(line["quantity"] or 0) for line in order_data["order_lines"]}
        for line_id, qty in parsed_partial.items():
            try:
                qty_float = float(qty)
            except (TypeError, ValueError):
                raise HTTPException(status_code=422, detail=f"Invalid quantity for line {line_id}")
            if qty_float < 0:
                raise HTTPException(status_code=422, detail=f"Dispatched quantity cannot be negative (line {line_id})")
            if line_id in ordered_map and qty_float > ordered_map[line_id]:
                raise HTTPException(
                    status_code=422,
                    detail=f"Dispatched quantity ({qty_float}) exceeds ordered quantity ({ordered_map[line_id]}) for line {line_id}"
                )

    # --- Regenerate XML ---
    try:
        xml_content = generate_despatch_advice(
            order_data,
            carrier,
            dispatch_date,
            notes,
            partial_lines=parsed_partial,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # --- Update record in place (preserve uuid + despatch_id) ---
    despatch.xml_content = xml_content
    despatch.source_order_xml = order_xml_str
    despatch.updated_at = datetime.utcnow()
    db.commit()

    filename = f"Despatch_{despatch.despatch_id}_{despatch.uuid}.xml"

    return StreamingResponse(
        io.BytesIO(xml_content.encode("utf-8")),
        media_type="application/xml",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Despatch-UUID": despatch.uuid,
        }
    )

# # Wipes the entire database
# @router.delete("/admin/wipe")
# def wipe_all_despatches(
#     db: Session = Depends(get_db),
#     user: User = Depends(get_current_user)
# ):
#     # --- Admin check ---
#     if not user.is_admin:
#         raise HTTPException(status_code=403, detail="Admin privileges required")

#     # --- Delete everything ---
#     deleted = db.query(Despatch).delete()
#     db.commit()

#     return {
#         "message": "All despatch records deleted",
#         "deleted_count": deleted
#     }
