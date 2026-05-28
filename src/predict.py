import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

def predict_price(surface: float, rooms: int):

    data = pd.DataFrame([{
        "surface": surface,
        "rooms": rooms
    }])

    prediction = model.predict(data)[0]

    return round(prediction, 2)
