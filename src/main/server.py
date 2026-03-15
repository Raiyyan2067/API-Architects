from fastapi import FastAPI, HTTPException, Response
from despatch_models import DespatchRequest

from main import testMessage
from ubl_generator import generate_despatch_advice

app = FastAPI()

@app.get("/")
def root():
    return testMessage()

# Create a new UBL Despatch Advice document
@app.post("/ubl/v2/despatch-advice")
def create_despatch_advice(request: DespatchRequest):
    try:
        xml = generate_despatch_advice(request)

        return Response(
            content=xml,
            media_type="application/xml"
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Retrieve a list of all Despatch Advice documents
@app.get("/ubl/v2/despatch-advice")
def list_despatch_advice():
    return {"message": "list_despatch_advice stub is working"}

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
    return {"message": "health_check stub is working"}