import pandas as pd
import mlflow

mlflow.set_tracking_uri("http://mlflow:5000")

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