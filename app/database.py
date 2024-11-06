from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

MYSQL_ADDON_USER = os.getenv("MYSQL_ADDON_USER")
MYSQL_ADDON_PASSWORD = os.getenv("MYSQL_ADDON_PASSWORD")
MYSQL_ADDON_HOST = os.getenv("MYSQL_ADDON_HOST")
MYSQL_ADDON_DB = os.getenv("MYSQL_ADDON_DB")
MYSQL_ADDON_PORT = os.getenv("MYSQL_ADDON_PORT")

DATABASE_URL = f"mysql+pymysql://{MYSQL_ADDON_USER}:{MYSQL_ADDON_PASSWORD}@{MYSQL_ADDON_HOST}:{MYSQL_ADDON_PORT}/{MYSQL_ADDON_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
