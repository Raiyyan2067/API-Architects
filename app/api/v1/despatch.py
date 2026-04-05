from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
import os
import io
from uuid import uuid4
from datetime import datetime, timezone

# Updated imports to match new project structure
from app.core.ubl_generator import generate_despatch_advice
from app.models.despatch_models import DespatchRequest
from sqlalchemy.orm import Session
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
def generate_despatch(
    request: DespatchRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # Generate the XML content
    xml_content = generate_despatch_advice(request)
    
    # Generate a unique UUID for this despatch
    doc_uuid = str(uuid4())

    # Save the despatch in the database
    despatch = Despatch(
        uuid=doc_uuid,
        despatch_id=request.despatch_id,
        xml_content=xml_content,
        user_id=user.id
    )
    
    db.add(despatch)
    db.commit()

    # Convert XML string to a BytesIO stream for download
    xml_stream = io.BytesIO(xml_content.encode("utf-8"))
    filename = f"Despatch_{request.despatch_id}_{doc_uuid}.xml"

    # Return as a downloadable file
    return StreamingResponse(
        xml_stream,
        media_type="application/xml",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Despatch-UUID": doc_uuid,
            "Despatch-ID": request.despatch_id,
        },
        status_code=201
    )


# Returns list of all of a user's generated XML documents
@router.get("/list")
def list_despatch_advice():
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