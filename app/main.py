from fastapi import FastAPI
from app.api.v1 import despatch, health

app = FastAPI()


@app.get("/")
def root():
    return {"message": "UBL API is running"}


app.include_router(despatch.router, prefix="/ubl/v2/despatch-advice")
app.include_router(health.router, prefix="/ubl/v2/despatch-advice")
