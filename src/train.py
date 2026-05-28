import os
import joblib
import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.DataFrame({
    "surface": [50, 60, 80, 100, 120, 150],
    "rooms": [2, 3, 3, 4, 5, 6],
    "price": [150000, 180000, 240000, 300000, 360000, 450000]
})

X = data[["surface", "rooms"]]
y = data["price"]

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("house-price-minio")

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    mae = mean_absolute_error(y, predictions)
    mse = mean_squared_error(y, predictions)

    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("features", "surface,rooms")

    mlflow.log_metric("mae", mae)
    mlflow.log_metric("mse", mse)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

    mlflow.sklearn.log_model(model, "model")

    print("Model saved")
    print(f"MAE: {mae}")
    print(f"MSE: {mse}")
