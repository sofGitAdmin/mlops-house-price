import pandas as pd
import mlflow
import os

mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
)

_model = None


def get_model():
    global _model

    if _model is None:
        _model = mlflow.pyfunc.load_model(
            "models:/house-price-model@production"
        )

    return _model


def predict_price(surface, rooms):
    model = get_model()

    df = pd.DataFrame([
        {
            "surface": surface,
            "rooms": rooms
        }
    ])

    prediction = model.predict(df)[0]

    return float(prediction)