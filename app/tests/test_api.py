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
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    print("Root endpoint test passed")

def test_create_patient():
    """Test creating a patient"""
    response = client.post("/api/patients/", json=sample_patient)
    assert response.status_code == 200
    data = response.json()
    assert "age" in data
    assert data["age"] == sample_patient["age"]
    print("Create patient test passed")

def test_get_patients():
    """Test getting all patients"""
    response = client.get("/api/patients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print("Get patients test passed")

def test_predict_risk():
    """Test predicting cardiovascular risk"""
    response = client.post("/api/predict/", json=sample_patient)
    assert response.status_code == 200
    data = response.json()
    
    # Check that response contains expected fields
    assert "risk_score" in data or "prediction" in data or "risk" in data
    
    # Verify the prediction is a valid value (adjust based on your model output)
    if "risk_score" in data:
        assert isinstance(data["risk_score"], (int, float))
        assert 0 <= data["risk_score"] <= 1  # Assuming probability between 0 and 1
    
    print(f"Predict risk test passed - Result: {data}")

if __name__ == "__main__":
    print("Running API tests...\n")
    test_root()
    test_create_patient()
    test_get_patients()
    test_predict_risk()
    print("\nAll tests passed!")
