from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientResponse
from app.core.database import get_db


router = APIRouter()

@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    """Get all patients from the database"""
    patients = db.query(Patient).all()
    return patients


@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    """Create a new patient without prediction"""
    new_patient = Patient(**patient.dict(), status=None)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient