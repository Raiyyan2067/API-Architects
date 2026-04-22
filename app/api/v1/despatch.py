from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
import io
import json

from app.core.order_parser import parse_ubl_order
from app.core.ubl_generator import generate_despatch_advice, validate_xml_against_xsd
from app.models.user_models import User, Despatch
from app.data.db import get_db
from app.core.auth import get_current_user

router = APIRouter(tags=["Despatch Advice (v3)"])


@router.post(
    "/validate",
    summary="Validate a UBL XML document",
    description="""
Upload any XML file to validate it against the UBL 2.1 DespatchAdvice XSD schema.

No authentication required — this endpoint is publicly accessible.

**Returns:** `{ "valid": true }` if the document passes, or `{ "valid": false, "errors": ["..."] }` with a list of schema violations if it fails.
    """,
    responses={
        200: {"description": "Validation result — check the `valid` field"},
        400: {"description": "No file uploaded or empty file"},
    }
)
async def validate_xml(
    file: UploadFile = File(..., description="XML file to validate against the UBL 2.1 DespatchAdvice XSD schema"),
):
    xml_bytes = await file.read()
    if not xml_bytes:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    try:
        validate_xml_against_xsd(xml_bytes.decode("utf-8"))
        return {"valid": True, "errors": []}
    except ValueError as e:
        return {"valid": False, "errors": [str(e)]}
    except Exception as e:
        return {"valid": False, "errors": [f"Unexpected error: {str(e)}"]}


@router.post(
    "/generate",
    status_code=201,
    summary="Generate a Despatch Advice",
    description="""
Upload a UBL 2.1 Order XML file to generate a fully compliant UBL 2.1 Despatch Advice XML document.

**Partial orders:** Supply `partial_lines` as a JSON string mapping each line `ID` to the quantity
being dispatched (e.g. `{"1": 60, "2": 100}`). Any line with a dispatched quantity less than the
ordered quantity will automatically include `BackorderQuantity` and `BackorderReason` fields in the
output XML. If `partial_lines` is omitted, all lines are dispatched in full.

**Auth:** Requires a valid Bearer token. The generated document is stored against the authenticated user.

**Returns:** Streaming XML file download. The assigned UUID is also returned in the `Despatch-UUID` response header.
    """,
    responses={
        201: {"description": "Despatch Advice XML file generated and returned as a download"},
        400: {"description": "Empty file uploaded"},
        401: {"description": "Missing or invalid Bearer token"},
        422: {"description": "Invalid XML, unrecognised Order format, or partial_lines validation failure"},
        500: {"description": "XML generation or XSD validation error"},
    }
)
async def generate_despatch(
    order_xml: UploadFile = File(..., description="UBL 2.1 Order XML file to generate the despatch from"),
    carrier: str = Form("", description="Carrier name (e.g. Australia Post, DHL). Mapped to CarrierParty in the output XML."),
    dispatch_date: str = Form("", description="Dispatch date in YYYY-MM-DD format. Defaults to today if omitted."),
    notes: str = Form("", description="Optional delivery notes. Appears as a document-level Note element in the XML."),
    partial_lines: str = Form("", description='Optional JSON string mapping line IDs to dispatched quantities. Example: {"1": 60, "2": 100}. Omit to dispatch all lines in full.'),
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
@router.get("/list", summary="List your despatch documents", description="Returns all despatch documents belonging to the authenticated user.")
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
@router.get("/admin/list", summary="[Admin] List all despatches", description="Returns all despatch documents across all users. Admin only.")
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


# ── Static-segment routes MUST come before wildcard routes ───
# Order matters: /id/download/{id} and /id/{id}/source-order must be
# registered before /id/{id} otherwise FastAPI matches the wildcard first.

# Download the XML file for a Despatch Advice using its ID
@router.get("/id/download/{id}", summary="Download despatch XML by ID", description="Streams the XML file as a downloadable attachment, identified by despatch_id.")
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
@router.get("/uuid/download/{uuid}", summary="Download despatch XML by UUID", description="Streams the XML file as a downloadable attachment, identified by UUID.")
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


@router.get(
    "/id/{id}/source-order",
    summary="Get source Order XML for a despatch",
    description="""
Returns the original UBL 2.1 Order XML that was uploaded when this despatch was first generated.

This endpoint exists to support the **edit flow** — the frontend fetches this XML to repopulate
the line item quantity inputs before the user submits an update via `PUT /id/{id}/edit`.

Note: despatches created before this feature was introduced will not have a stored source order
and will return 404.

**Auth:** Requires Bearer token. Only the owner or an admin can access this.
    """,
    responses={
        200: {"description": "Original Order XML returned as application/xml"},
        401: {"description": "Missing or invalid Bearer token"},
        403: {"description": "Authenticated user does not own this despatch"},
        404: {"description": "Despatch not found, or no source order XML stored for this record"},
    }
)
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


# ── Wildcard routes come AFTER all static-segment routes ─────

# Retrieve a Despatch Advice document using its ID
@router.get("/id/{id}", summary="Get despatch XML by ID", description="Returns the raw UBL XML content of a despatch by its despatch_id.")
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
@router.get("/uuid/{uuid}", summary="Get despatch XML by UUID", description="Returns the raw UBL XML content of a despatch by its UUID.")
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


# Delete a Despatch Advice document using its ID
@router.delete("/id/{id}", summary="Delete a despatch by ID", description="Deletes a despatch record by its despatch_id. Only the owner or an admin can delete.")
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
@router.delete(
    "/uuid/{uuid}",
    summary="Delete a despatch by UUID",
    description="Deletes a despatch record by its UUID. Only the owner or an admin can delete.",
    responses={
        200: {"description": "Deleted successfully"},
        401: {"description": "Missing or invalid Bearer token"},
        403: {"description": "Not the owner or admin"},
        404: {"description": "Despatch not found"},
    }
)
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


@router.put(
    "/id/{id}/edit",
    summary="Edit and regenerate an existing despatch",
    description="""
Regenerates an existing Despatch Advice with updated inputs. The original `despatch_id` and `UUID`
are preserved — only the XML content and metadata are replaced.

**Order XML:** If a new `order_xml` file is uploaded it replaces the stored source order for this
record. If omitted, the original Order XML stored at generation time is re-used automatically.
If neither is available a 422 is returned.

**Partial orders:** Same `partial_lines` JSON format as `/generate` — supply a mapping of line IDs
to dispatched quantities to update which lines are partially shipped.

**Auth:** Requires Bearer token. Only the owner or an admin can edit a despatch.

**Returns:** Streaming XML file download of the regenerated despatch. Same `Despatch-UUID` header
as the original.
    """,
    responses={
        200: {"description": "Updated Despatch Advice XML returned as a download"},
        400: {"description": "Empty file uploaded"},
        401: {"description": "Missing or invalid Bearer token"},
        403: {"description": "Authenticated user does not own this despatch"},
        404: {"description": "Despatch not found"},
        422: {"description": "No Order XML available, invalid XML, or partial_lines validation failure"},
        500: {"description": "XML generation or XSD validation error"},
    }
)
async def edit_despatch(
    id: str,
    order_xml: UploadFile = File(None, description="Optional replacement Order XML. If omitted, the originally uploaded Order XML is re-used."),
    carrier: str = Form("", description="Updated carrier name."),
    dispatch_date: str = Form("", description="Updated dispatch date in YYYY-MM-DD format."),
    notes: str = Form("", description="Updated delivery notes."),
    partial_lines: str = Form("", description='Optional JSON string mapping line IDs to dispatched quantities. Example: {"1": 40}. Omit to dispatch all lines in full.'),
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
            detail="No Order XML provided and no source order stored — please upload the original Order XML"
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
