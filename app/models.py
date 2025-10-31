from sqlalchemy import create_engine, Column, Integer, String
from database import Base 

class patient(Base):
    __tabelname__ = 'patients'

