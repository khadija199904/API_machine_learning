from fastapi import FastAPI
from app.api import patients
from app.core.database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cardio Risk API",
    description="Predict cardiovascular risk and manage patients.",
    version="1.0.0"
)

# Include patient routes
app.include_router(patients.router, prefix="/api", tags=["Patients"])

@app.get("/")
def root():
    return {"message": "Cardio Risk API is running!"}
