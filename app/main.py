from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth, despatch, old_despatch, health
from mangum import Mangum

from app.data.db import engine, Base
from app.models import user_models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="UBL Despatch API", version="2.1")

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Use ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "UBL API is running"}

app.include_router(auth.router, prefix="/ubl/auth")
app.include_router(despatch.router, prefix="/ubl/v3/despatch-advice")
app.include_router(old_despatch.router, prefix="/ubl/v2/despatch-advice")
app.include_router(health.router, prefix="/ubl/v2/despatch-advice")

handler = Mangum(app)