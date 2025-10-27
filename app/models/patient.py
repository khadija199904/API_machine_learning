from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    cholesterol = Column(Float, nullable=False)
    blood_pressure = Column(Float, nullable=False)
