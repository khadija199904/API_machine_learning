from pydantic import BaseModel
# import joblib

# Load the pre-trained model when the application starts
# model = joblib.load('best_pipeline_XGBoost.pkl')
class PatientBase(BaseModel):
    age: int
    gender: int
    pressurehight: float
    pressurelow: float
    glucose: float
    kcm: float
    troponin: float
    impluse: float

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    status: int | None = None

    class Config:
        from_attributes = True
