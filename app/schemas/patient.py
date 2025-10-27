from pydantic import BaseModel

class PatientBase(BaseModel):
    age: int
    gender: int
    pressurehight: float
    pressurelow: float
    glucose: float
    kcm: float
    troponin: float
    impluse: int
    status: str

class PatientCreate(PatientBase):
    pass

class PatientShow(PatientBase):
    id: int

    class Config:
        from_attributes = True
