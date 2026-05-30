from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "running"}


def test_predict(monkeypatch):
    def fake_predict_price(surface, rooms):
        return 270000.0

    monkeypatch.setattr(
        "app.main.predict_price",
        fake_predict_price
    )

    response = client.post(
        "/predict",
        json={
            "surface": 90,
            "rooms": 4
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "predicted_price": 270000.0
    }