from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

from src.predict import predict_price

app = FastAPI()

Instrumentator().instrument(app).expose(app)

class HouseInput(BaseModel):
    surface: float
    rooms: int

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/predict")
def predict(data: HouseInput):
    prediction = predict_price(data.surface, data.rooms)
    return {"predicted_price": prediction}