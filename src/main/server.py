from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from main import generate_despatch_advice
from despatch_models import DespatchRequest
import os
from uuid import uuid4
from datetime import datetime

app = FastAPI()

# Temp database to store generated XML file (no persistence)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATED_DIR = os.path.join(BASE_DIR, "generated")
os.makedirs(GENERATED_DIR, exist_ok=True)

TEMP_FILE = {"uuid": None, "file_path": None}

@app.get("/")
def root():
    return {"message": "Hello World! I am root!"}

# Create a new UBL Despatch Advice document
@app.post("/ubl/v2/despatch-advice/generate", status_code=201)
def generate_despatch(request: DespatchRequest):
    try:
        xml_content = generate_despatch_advice(request)
        doc_uuid = str(uuid4())
        time_created = datetime.utcnow().strftime("%Y%m%dT%H%M%S")

        filename = f"Despatch_{request.despatch_id}_{doc_uuid}_{time_created}.xml"
        file_path = os.path.join(GENERATED_DIR, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(xml_content)

        TEMP_FILE["uuid"] = doc_uuid
        TEMP_FILE["file_path"] = file_path

        return FileResponse(
            TEMP_FILE["file_path"],
            media_type="application/xml",
            filename=f"Despatch_{TEMP_FILE['uuid']}.xml",
            headers={
                "Despatch-UUID": doc_uuid,
                "Despatch-ID": request.despatch_id,
                "Message": "Despatch Advice successfully created"
            }
        )
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Retrieve a list of all Despatch Advice documents
@app.get("/ubl/v2/despatch-advice/list")
def list_despatch_advice():
    if not TEMP_FILE["file_path"]:
        raise HTTPException(status_code=404, detail="No Despatch Advice generated yet")
    return FileResponse(TEMP_FILE["file_path"], media_type="application/xml", filename=f"Despatch_{TEMP_FILE['uuid']}.xml")

# Retrieve a Despatch Advice document using its ID
@app.get("/ubl/v2/despatch-advice/id/{id}")
def get_despatch_advice_by_id(id: str):
    return {
        "message": "get_despatch_advice_by_id stub is working",
        "id": id
    }

# Retrieve a Despatch Advice document using its UUID
@app.get("/ubl/v2/despatch-advice/uuid/{uuid}")
def get_despatch_advice_by_uuid(uuid: str):
    return {
        "message": "get_despatch_advice_by_uuid stub is working",
        "uuid": uuid
    }

# Validate a Despatch Advice XML against the UBL schema
@app.post("/ubl/v2/despatch-advice/validate")
def validate_despatch_advice():
    return {"message": "validate_despatch_advice stub is working"}

# Download the XML file for a Despatch Advice using its ID
@app.get("/ubl/v2/despatch-advice/id/download/{id}")
def download_despatch_advice_by_id(id: str):
    return {
        "message": "download_despatch_advice_by_id stub is working",
        "id": id
    }

# Download the XML file for a Despatch Advice using its UUID
@app.get("/ubl/v2/despatch-advice/uuid/download/{uuid}")
def download_despatch_advice_by_uuid(uuid: str):
    return {
        "message": "download_despatch_advice_by_uuid stub is working",
        "uuid": uuid
    }

# Delete a Despatch Advice document using its ID
@app.delete("/ubl/v2/despatch-advice/id/{id}")
def delete_despatch_advice_by_id(id: str):
    return {
        "message": "delete_despatch_advice_by_id stub is working",
        "id": id
    }

# Delete a Despatch Advice document using its UUID
@app.delete("/ubl/v2/despatch-advice/uuid/{uuid}")
def delete_despatch_advice_by_uuid(uuid: str):
    return {
        "message": "delete_despatch_advice_by_uuid stub is working",
        "uuid": uuid
    }

# Health check to confirm the service is running
@app.get("/ubl/v2/despatch-advice/health")
def health_check():
    return {"status": "ok"}