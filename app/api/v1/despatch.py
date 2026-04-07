from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime, timezone
import io
import os

from app.core.order_parser import parse_ubl_order
from app.core.ubl_generator import generate_despatch_advice
from app.models.user_models import User, Despatch
from app.data.db import get_db
from app.core.auth import get_current_user

router = APIRouter(tags=["Despatch Advice (v2)"])

# Validate an incoming Order XML against the UBL schema


@router.post("/validate")
def validate_order():
    return {"message": "validate_despatch_advice stub is working"}


# Generatres an XML despatch advice file from a XML Order and returns a download to the generated file


@router.post("/generate", status_code=201)
async def generate_despatch(
    order_xml: UploadFile = File(...),
    carrier: str = Form(""),
    dispatch_date: str = Form(""),
    notes: str = Form(""),
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

    # --- Generate ---
    try:
        xml_content = generate_despatch_advice(
            order_data,
            carrier,
            dispatch_date,
            notes
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # --- Store ---
    doc_uuid = str(uuid4())

    despatch = Despatch(
        uuid=doc_uuid,
        despatch_id=order_data["order_id"],
        xml_content=xml_content,
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
def list_despatch_advice():
    return

# Returns list of all generated XML documents (admin only)


@router.delete("/uuid/{uuid}")
def list_all_despatch_advice():
    return

# Retrieve a Despatch Advice document using its ID


@router.get("/id/{id}")
def get_despatch_advice_by_id(id: str):
    return {
        "message": "get_despatch_advice_by_id stub is working",
        "id": id
    }


# Retrieve a Despatch Advice document using its UUID
@router.get("/uuid/{uuid}")
def get_despatch_advice_by_uuid(uuid: str):
    return {
        "message": "get_despatch_advice_by_uuid stub is working",
        "uuid": uuid
    }


# Download the XML file for a Despatch Advice using its ID
@router.get("/id/download/{id}")
def download_despatch_advice_by_id(id: str):
    return {
        "message": "download_despatch_advice_by_id stub is working",
        "id": id
    }


# Download the XML file for a Despatch Advice using its UUID
@router.get("/uuid/download/{uuid}")
def download_despatch_advice_by_uuid(uuid: str):
    return {
        "message": "download_despatch_advice_by_uuid stub is working",
        "uuid": uuid
    }


# Delete a Despatch Advice document using its ID
@router.delete("/id/{id}")
def delete_despatch_advice_by_id(id: str):
    return {
        "message": "delete_despatch_advice_by_id stub is working",
        "id": id
    }


# Delete a Despatch Advice document using its UUID
@router.delete("/uuid/{uuid}")
def delete_despatch_advice_by_uuid(uuid: str):
    return {
        "message": "delete_despatch_advice_by_uuid stub is working",
        "uuid": uuid
    }
