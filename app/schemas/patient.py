from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    cholesterol: float
    blood_pressure: float

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int

    class Config:
        orm_mode = True
