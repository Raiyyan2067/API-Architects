from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from app.data.db import get_db
from app.models.db_models import User
from sqlalchemy.orm import Session

SUPER_SECRET_KEY = "9f8c1e7c8b2a4f3d9e6a1c0b7d4e2f8a6c5d3b1e9f7a2c4d6b8e0f1a3c5d7e9"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SUPER_SECRET_KEY, algorithm=ALGORITHM)


security = HTTPBearer()

def get_current_user(token=Depends(security), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token.credentials, SUPER_SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except:
        raise HTTPException(401, "Invalid token")

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(401, "User not found")

    return user