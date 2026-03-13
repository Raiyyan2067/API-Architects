from fastapi import FastAPI

from main import testMessage

app = FastAPI()

@app.get("/")
def root():
    return testMessage()

# Create a new UBL Despatch Advice document
@app.post("/ubl/v2/despatch-advice")
def create_despatch_advice():
    return {"message": "Endpoint stub is working"}

# Retrieve a list of all Despatch Advice documents
@app.get("/ubl/v2/despatch-advice")
def list_despatch_advice():
    return {"message": "Endpoint stub is working"}

# Retrieve a Despatch Advice document using its ID
@app.get("/ubl/v2/despatch-advice/id/{id}")
def get_despatch_advice_by_id(id: str):
    return {"message": "Endpoint stub is working"}

# Retrieve a Despatch Advice document using its UUID
@app.get("/ubl/v2/despatch-advice/uuid/{uuid}")
def get_despatch_advice_by_uuid(uuid: str):
    return {"message": "Endpoint stub is working"}

# Validate a Despatch Advice XML against the UBL schema
@app.post("/ubl/v2/despatch-advice/validate")
def validate_despatch_advice():
    return {"message": "Endpoint stub is working"}

# Download the XML file for a Despatch Advice using its ID
@app.get("/ubl/v2/despatch-advice/id/download/{id}")
def download_despatch_advice_by_id(id: str):
    return {"message": "Endpoint stub is working"}

# Download the XML file for a Despatch Advice using its UUID
@app.get("/ubl/v2/despatch-advice/uuid/download/{uuid}")
def download_despatch_advice_by_uuid(uuid: str):
    return {"message": "Endpoint stub is working"}

# Delete a Despatch Advice document using its ID
@app.delete("/ubl/v2/despatch-advice/id/{id}")
def delete_despatch_advice_by_id(id: str):
    return {"message": "Endpoint stub is working"}

# Delete a Despatch Advice document using its UUID
@app.delete("/ubl/v2/despatch-advice/uuid/{uuid}")
def delete_despatch_advice_by_uuid(uuid: str):
    return {"message": "Endpoint stub is working"}

# Health check to confirm the service is running
@app.get("/ubl/v2/despatch-advice/health")
def health_check():
    return {"message": "Endpoint stub is working"}