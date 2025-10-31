import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String



# Database setup
DATABASE_URL = "sqlite:///./patients.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

