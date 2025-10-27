from pydantic import BaseModel

# Schema to create a patient
class PatientCreate(BaseModel):
    age: int
    gender: int
    pressurehight: float
    pressurelow: float
    glucose: float
    kcm: float
    troponin: float
    impluse: float
    status: str

# Schema to return patient info
class PatientResponse(BaseModel):
    id: int
    age: int
    gender: int
    pressurehight: float
    pressurelow: float
    glucose: float
    kcm: float
    troponin: float
    impluse: float
    status: str

    class Config:
        from_attributes = True
