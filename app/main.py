from fastapi import FastAPI
from app.api.v1 import despatch, health
from mangum import Mangum

app = FastAPI(title="UBL Despatch API", version="2.1")

@app.get("/")
def root():
    return {"message": "UBL API is running"}

app.include_router(despatch.router, prefix="/ubl/v2/despatch-advice")
app.include_router(health.router, prefix="/ubl/v2/despatch-advice")

handler = Mangum(app)
