from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel
from app.data.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)

    despatches = relationship("Despatch", back_populates="user")

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class Despatch(Base):
    __tablename__ = "despatches"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True)
    despatch_id = Column(String)
    xml_content = Column(Text)
    source_order_xml = Column(Text, nullable=True)   # stores original uploaded Order XML for edit flow
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="despatches")