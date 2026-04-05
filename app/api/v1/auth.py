from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.data.db import get_db
from app.models.db_models import User, RegisterRequest, LoginRequest, TokenResponse
from app.core.auth import hash_password, verify_password, create_token, get_current_user

router = APIRouter(tags=["auth"])

@router.post("/register")
def register(user: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(400, "Username already exists")

    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered"}

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.id)
    return {"access_token": token}

@router.post("/logout")
def logout():
    return {"message": "Logout successful"}

@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return {"id": user.id, "username": user.username}