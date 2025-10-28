from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientResponse
from app.core.database import get_db
import joblib
import pandas as pd
from pathlib import Path

router = APIRouter()

# Path to your model file
MODEL_PATH = Path("app/models/best_pipeline_XGBoost.pkl")

# Load model safely
try:
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    model = None
    print(f"Could not load model: {e}")

# Prediction route
@router.post("/predict_risk", response_model=PatientResponse)
def predict_risk(patient: PatientCreate, db: Session = Depends(get_db)):
    """
    Predicts the patient's cardiovascular risk using the trained ML model,
    saves it in the database, and returns the full patient record.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded on server")

    # Convert to DataFrame for the model
    data = pd.DataFrame([patient.dict()])

    #  Make prediction
    try:
        prediction = model.predict(data)[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")

    # Save to DB
    db_patient = Patient(**patient.dict(), status=int(prediction))
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient
