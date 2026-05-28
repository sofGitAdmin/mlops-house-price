import pandas as pd
import mlflow

mlflow.set_tracking_uri("http://mlflow:5000")

model = mlflow.pyfunc.load_model(
    "models:/house-price-model@production"
)

def predict_price(surface, rooms):

    df = pd.DataFrame([
        {
            "surface": surface,
            "rooms": rooms
        }
    ])

    prediction = model.predict(df)[0]

    return float(prediction)