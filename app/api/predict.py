from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientResponse
from app.core.database import get_db
import joblib
import pandas as pd
from pathlib import Path

router = APIRouter()

MODEL_FILE = Path("app/models/best_pipeline_XGBoost.pkl")

try:
    model = joblib.load(MODEL_FILE)
    print(f"Model loaded: {MODEL_FILE}")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

# -------------------------------
#  Prediction endpoint
# -------------------------------
@router.post("/predict", response_model=PatientResponse)
def predict(patient: PatientCreate, db: Session = Depends(get_db)):
    """Predict cardiovascular risk and save the result in database."""
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Convert input to DataFrame
    df = pd.DataFrame([patient.dict()])

    # Make prediction
    try:
        prediction = int(model.predict(df)[0])
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")

    # Save prediction to DB
    new_patient = Patient(**patient.dict(), status=prediction)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient
