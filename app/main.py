from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.api.v1 import auth, despatch, old_despatch, health
from mangum import Mangum
from app.data.db import engine, Base, get_db
from app.models.user_models import User
from app.core.auth import hash_password

Base.metadata.create_all(bind=engine)

app = FastAPI(title="UBL Despatch API", version="2.1")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows specific origins
    allow_credentials=True,           # Allows cookies and auth headers
    # Allows all HTTP methods (GET, POST, etc.)
    allow_methods=["*"],
    allow_headers=["*"],              # Allows all headers
)


@app.get("/")
def root():
    return {"message": "UBL API is running"}


app.include_router(auth.router, prefix="/ubl/auth")
app.include_router(despatch.router, prefix="/ubl/v3/despatch-advice")
app.include_router(old_despatch.router, prefix="/ubl/v2/despatch-advice")
app.include_router(health.router, prefix="/ubl/v2/despatch-advice")

# --- Startup event to create admin ---


@app.on_event("startup")
def create_admin_user():
    db: Session = next(get_db())
    admin_user = db.query(User).filter(User.username == "admin").first()
    if not admin_user:
        new_admin = User(
            username="admin",
            hashed_password=hash_password("admin123"),
            is_admin=True
        )
        db.add(new_admin)
        db.commit()
        print("Admin user 'admin' created successfully!")
    else:
        print("Admin user already exists.")


handler = Mangum(app)
