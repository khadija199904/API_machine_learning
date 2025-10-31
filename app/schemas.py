from pydantic import BaseModel

class Patient(BaseModel):
    age: int
    gender: int
    pressurehight : float
    pressurelow : float
    glucose : float
    kcm : float
    troponin : int
    impluse : float

