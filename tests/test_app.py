import os
import subprocess
import json
import pytest
from pathlib import Path
from app import app, BASE_DIR

@pytest.fixture(scope="session")
def client():
    # Ensure the model is trained before any test runs
    model_path = Path(BASE_DIR) / "cancer_model.pkl"
    if not model_path.exists():
        subprocess.check_call(["python", "train_model.py"], cwd=os.path.abspath(os.path.dirname(__file__) + "../.."))
    app.testing = True
    with app.test_client() as client:
        yield client

def test_model_files_exist():
    assert (Path(BASE_DIR) / "cancer_model.pkl").exists()
    assert (Path(BASE_DIR) / "feature_names.pkl").exists()

def test_predict_success(client):
    payload = {
        "mean radius": 17.99, "mean texture": 10.38, "mean perimeter": 122.8,
        "mean area": 1001.0, "mean smoothness": 0.1184, "mean compactness": 0.2776,
        "mean concavity": 0.3001, "mean concave points": 0.1471,
        "mean symmetry": 0.2419, "mean fractal dimension": 0.07871,
        "radius error": 1.095, "texture error": 0.9053, "perimeter error": 8.589,
        "area error": 153.4, "smoothness error": 0.006399,
        "compactness error": 0.04904, "concavity error": 0.05373,
        "concave points error": 0.01587, "symmetry error": 0.03003,
        "fractal dimension error": 0.006193,
        "worst radius": 25.38, "worst texture": 17.33, "worst perimeter": 184.6,
        "worst area": 2019.0, "worst smoothness": 0.1622,
        "worst compactness": 0.6656, "worst concavity": 0.7119,
        "worst concave points": 0.2654, "worst symmetry": 0.4601,
        "worst fractal dimension": 0.1189
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data
    assert data["prediction"] in ("Malignant", "Benign")

def test_missing_feature(client):
    # Only provide a subset of required fields
    payload = {"mean radius": 17.99}
    response = client.post("/predict", json=payload)
    assert response.status_code == 400
    assert "Missing required features" in response.get_json()["error"]

def test_invalid_content_type(client):
    # Send form encoded data instead of JSON
    response = client.post("/predict", data="foo=bar", headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 415
    assert "Invalid content type" in response.get_json()["error"]
