from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

sample_patient = {
    "age": 45,
    "gender": 1,
    "pressurehight": 140.0,
    "pressurelow": 90.0,
    "glucose": 110.0,
    "kcm": 4.5,
    "troponin": 0.03,
    "impluse": 70.0
}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    print("✓ Root endpoint test passed")

def test_create_patient():
    response = client.post("/api/patients/", json=sample_patient)
    assert response.status_code == 200
    data = response.json()
    assert data["age"] == sample_patient["age"]
    print("✓ Create patient test passed")

def test_get_patients():
    response = client.get("/api/patients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print("✓ Get patients test passed")

def test_predict_risk():
    response = client.post("/api/predict/", json=sample_patient)
    assert response.status_code == 200
    data = response.json()
    print(f"✓ Predict risk test passed - Risk: {data}")
