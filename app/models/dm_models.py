from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.data.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)

    despatches = relationship("Despatch", back_populates="user")


class Despatch(Base):
    __tablename__ = "despatches"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True)
    despatch_id = Column(String)
    xml_content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="despatches")