from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

app = FastAPI(title="Heart Disease Prediction API")

# Load trained model
model = joblib.load("../model/heart_disease_model.pkl")

class PatientData(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_blood_pressure: int
    cholesterol: int
    fasting_blood_sugar: int
    resting_ecg: int
    max_heart_rate: int
    exercise_induced_angina: int
    st_depression: float
    st_slope: int
    num_major_vessels: int
    thalassemia: int


@app.get("/")
def home():
    return {"message": "Heart Disease API Running"}


@app.post("/predict")
def predict(data: PatientData):

    input_data = np.array([
        data.age,
        data.sex,
        data.chest_pain_type,
        data.resting_blood_pressure,
        data.cholesterol,
        data.fasting_blood_sugar,
        data.resting_ecg,
        data.max_heart_rate,
        data.exercise_induced_angina,
        data.st_depression,
        data.st_slope,
        data.num_major_vessels,
        data.thalassemia
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }


# Run directly using python main.py
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
