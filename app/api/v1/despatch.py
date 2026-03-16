from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from uuid import uuid4
from datetime import datetime, timezone
import boto3

# Updated imports to match new project structure
from app.core.ubl_generator import generate_despatch_advice, parse_filename
from app.models.despatch_models import DespatchRequest

router = APIRouter()

s3 = boto3.client("s3")
BUCKET_NAME = "ubl-despatch-files"

# Adjusted BASE_DIR to point to the root from app/api/v1/
# Goes up 3 levels: v1 -> api -> app -> project_root
GENERATED_DIR = "/tmp/generated"
os.makedirs(GENERATED_DIR, exist_ok=True)

TEMP_FILE = {"uuid": None, "file_path": None}

# Create a new UBL Despatch Advice document


@router.post("/generate", status_code=201)
def generate_despatch(request: DespatchRequest):
    try:
        xml_content = generate_despatch_advice(request)
        doc_uuid = str(uuid4())
        time_created = datetime.now(timezone.utc).strftime("%Y-%m-%dT-%H%M%S")

        filename = f"Despatch_{request.despatch_id}_{doc_uuid}_{time_created}.xml"
        file_path = os.path.join(GENERATED_DIR, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(xml_content)

        TEMP_FILE["uuid"] = doc_uuid
        TEMP_FILE["file_path"] = file_path

        return FileResponse(
            TEMP_FILE["file_path"],
            media_type="application/xml",
            filename=f"Despatch_{request.despatch_id}_{doc_uuid}_{time_created}.xml",
            status_code = 201,
            headers={
                "Despatch-UUID": doc_uuid,
                "Despatch-ID": request.despatch_id,
                "Message": "Despatch Advice successfully created"
            }
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Retrieve a list of all Despatch Advice documents


@router.get("/list")
def list_despatch_advice():
    files = os.listdir(GENERATED_DIR)
    xml_files = [f for f in files]
    if not xml_files:
        raise HTTPException(
            status_code=404, detail="No Despatch Advice generated yet")

    file_data = [parse_filename(f) for f in xml_files]
    return {"files": file_data}

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
