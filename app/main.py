from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from mlflow.tracking import MlflowClient
from src.predict import predict_price
import os

app = FastAPI()

Instrumentator().instrument(app).expose(app)

class HouseInput(BaseModel):
    surface: float
    rooms: int

@app.get("/model-info")
def model_info():
    client = MlflowClient(
        tracking_uri=os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    )

    model_version = client.get_model_version_by_alias(
        name="house-price-model",
        alias="production"
    )

    return {
        "model_name": "house-price-model",
        "alias": "production",
        "version": model_version.version,
        "status": model_version.status,
        "run_id": model_version.run_id
    }
@app.get("/")
def root():
    return {"status": "running"}

@app.post("/predict")
def predict(data: HouseInput):
    prediction = predict_price(data.surface, data.rooms)
    return {"predicted_price": prediction}