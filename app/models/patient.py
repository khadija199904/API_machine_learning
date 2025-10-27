from sqlalchemy import Column, Integer, Float, String
from  app.core.database import  Base
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(Integer)  # 1 = Homme, 0 = Femme
    pressurehight = Column(Float)
    pressurelow = Column(Float)
    glucose = Column(Float)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Integer)
    status = Column(String)  # "positive" ou "negative"
