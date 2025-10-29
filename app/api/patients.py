from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientResponse
from app.core.database import get_db


router = APIRouter()
@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients 


@router.post("/", response_model=PatientCreate)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient
