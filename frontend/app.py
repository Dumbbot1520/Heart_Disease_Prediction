import streamlit as st
import requests

st.title("Heart Disease Prediction App")

st.write("Enter patient details below:")

age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex (0=Female, 1=Male)", [0,1])
chest_pain_type = st.selectbox("Chest Pain Type", [0,1,2,3])
resting_blood_pressure = st.number_input("Resting Blood Pressure", value=120)
cholesterol = st.number_input("Cholesterol", value=200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar >120", [0,1])
resting_ecg = st.selectbox("Resting ECG", [0,1,2])
max_heart_rate = st.number_input("Max Heart Rate", value=150)
exercise_induced_angina = st.selectbox("Exercise Induced Angina", [0,1])
st_depression = st.number_input("ST Depression", value=1.0)
st_slope = st.selectbox("ST Slope", [0,1,2])
num_major_vessels = st.selectbox("Number of Major Vessels", [0,1,2,3])
thalassemia = st.selectbox("Thalassemia", [0,1,2,3])

if st.button("Predict"):

    data = {
        "age": age,
        "sex": sex,
        "chest_pain_type": chest_pain_type,
        "resting_blood_pressure": resting_blood_pressure,
        "cholesterol": cholesterol,
        "fasting_blood_sugar": fasting_blood_sugar,
        "resting_ecg": resting_ecg,
        "max_heart_rate": max_heart_rate,
        "exercise_induced_angina": exercise_induced_angina,
        "st_depression": st_depression,
        "st_slope": st_slope,
        "num_major_vessels": num_major_vessels,
        "thalassemia": thalassemia
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]
        probability = result["probability"]

        if prediction == 1:
            st.error(f"⚠ High Risk of Heart Disease\nProbability: {probability:.2f}")
        else:
            st.success(f"✅ Low Risk of Heart Disease\nProbability: {probability:.2f}")
    else:
        st.error("Backend not running!")
