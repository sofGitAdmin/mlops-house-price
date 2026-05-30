import requests

BASE_URL = "http://localhost:8000"


def test_health_check():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_predict():
    payload = {
        "surface": 90,
        "rooms": 4
    }

    response = requests.post(f"{BASE_URL}/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "predicted_price" in data
    assert isinstance(data["predicted_price"], float)


def test_model_info():
    response = requests.get(f"{BASE_URL}/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["model_name"] == "house-price-model"
    assert data["alias"] == "production"
    assert "version" in data
    assert "run_id" in data