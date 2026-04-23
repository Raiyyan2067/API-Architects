import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PostgreSQL connection URL
DATABASE_URL = DATABASE_URL = "postgresql+psycopg2://postgres:6234qQ3!@ubl-db.c7essasc8gi8.ap-southeast-2.rds.amazonaws.com:5432/postgres"

# Create engine (no check_same_thread for PostgreSQL)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)  # pool_pre_ping helps keep RDS connections alive

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()