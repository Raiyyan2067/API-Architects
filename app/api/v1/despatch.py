from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
import os
import io
from uuid import uuid4
from datetime import datetime, timezone
import boto3

# Updated imports to match new project structure
from app.core.ubl_generator import generate_despatch_advice
from app.models.despatch_models import DespatchRequest
from sqlalchemy.orm import Session
from app.models.db_models import User, Despatch
from app.data.db import get_db
from app.core.auth import get_current_user

router = APIRouter()

s3 = boto3.client("s3")
BUCKET_NAME = "ubl-despatch-files-393035998882-ap-southeast-2-an"

# Adjusted BASE_DIR to point to the root from app/api/v1/
# Goes up 3 levels: v1 -> api -> app -> project_root
GENERATED_DIR = "/tmp/generated"
os.makedirs(GENERATED_DIR, exist_ok=True)


# Create a new UBL Despatch Advice document

@router.post("/generate", status_code=201)
def generate_despatch(request: DespatchRequest):
    try:
        # Generate XML content
        xml_content = generate_despatch_advice(request)
        doc_uuid = str(uuid4())
        time_created = datetime.now(timezone.utc).strftime("%Y-%m-%dT-%H%M%S")

        # S3 file name
        filename = f"Despatch_{request.despatch_id}_{doc_uuid}_{time_created}.xml"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=xml_content,
            ContentType="application/xml",
            ACL="public-read"  
        )

        # Stream from S3
        s3_obj = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
        stream = io.BytesIO(s3_obj['Body'].read())

        # Set headers
        headers = {
            "Despatch-UUID": doc_uuid,
            "Despatch-ID": request.despatch_id,
            "Message": "Despatch Advice successfully created"
        }

        return StreamingResponse(
            stream,
            media_type="application/xml",
            headers=headers,
            status_code=201
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/v2/generate", status_code=201)
def generate_despatch(
    request: DespatchRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    xml_content = generate_despatch_advice(request)

    doc_uuid = str(uuid4())

    despatch = Despatch(
        uuid=doc_uuid,
        despatch_id=request.despatch_id,
        xml_content=xml_content,
        user_id=user.id
    )

    db.add(despatch)
    db.commit()

    return {
        "message": "Despatch created",
        "uuid": doc_uuid
    }


# Returns list of all XML documents

@router.get("/list")
def list_despatch_advice():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    items = response.get("Contents", [])

    if not items:
        raise HTTPException(status_code=404, detail="No Despatch Advice generated yet")

    files = [{"key": f["Key"], "last_modified": f["LastModified"].isoformat()} for f in items]
    return {"files": files}

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

# Validate a Despatch Advice XML against the UBL schema


@router.post("/validate")
def validate_despatch_advice():
    return {"message": "validate_despatch_advice stub is working"}

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
