from flask import Flask, render_template, request
from xgboost import XGBClassifier
import numpy as np

app = Flask(__name__)

# Load trained XGBoost model
model = XGBClassifier()
model.load_model("cholera_xgboost_model.json")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    epi_week = int(request.form["epi_week"])
    suspected_cases = float(request.form["suspected_cases"])
    states_affected = float(request.form["states_affected"])
    weekly_rainfall = float(request.form["weekly_rainfall"])
    weekly_temperature = float(request.form["weekly_temperature"])
    rainfall_lag2 = float(request.form["rainfall_lag2"])
    rainfall_lag4 = float(request.form["rainfall_lag4"])
    temp_lag2 = float(request.form["temp_lag2"])

    # Calculate epidemiological week features
    epi_week_sin = np.sin(2 * np.pi * epi_week / 52)
    epi_week_cos = np.cos(2 * np.pi * epi_week / 52)

    # Arrange features in the same order used during model training
    features = np.array([[
        suspected_cases,
        states_affected,
        weekly_rainfall,
        weekly_temperature,
        rainfall_lag2,
        rainfall_lag4,
        temp_lag2,
        epi_week_sin,
        epi_week_cos
    ]])

    # Make prediction
    prediction = int(model.predict(features)[0])

    results = {
        0: {
            "level": "Level 0",
            "description": "No outbreak detected based on the model prediction."
        },
        1: {
            "level": "Level 1",
            "description": "Low outbreak level: 1–5 suspected cases."
        },
        2: {
            "level": "Level 2",
            "description": "Higher outbreak level: 6 or more suspected cases."
        }
    }

    result = results[prediction]

    return render_template(
        "index.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)