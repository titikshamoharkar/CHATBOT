# app.py
import streamlit as st
import numpy as np

st.set_page_config(page_title="Maternal Health Risk Predictor", layout="centered")

st.title("🤰 Maternal Health AI Risk Predictor")
st.write("Enter patient details to predict maternal health risk level.")

# User Inputs
age = st.number_input("Age", 15, 50)
systolic_bp = st.number_input("Systolic Blood Pressure", 80, 200)
diastolic_bp = st.number_input("Diastolic Blood Pressure", 60, 150)
blood_sugar = st.number_input("Blood Sugar Level", 4.0, 20.0)
body_temp = st.number_input("Body Temperature (°F)", 95.0, 105.0)
heart_rate = st.number_input("Heart Rate", 50, 150)

if st.button("Predict Risk"):
    input_data = np.array([[age, systolic_bp, diastolic_bp,
                            blood_sugar, body_temp, heart_rate]])
    # Mock prediction logic (replace with actual model inference)
    if age > 35 or systolic_bp > 140 or diastolic_bp > 90 or blood_sugar > 7.0 or body_temp > 100.4 or heart_rate > 100:
        prediction = ["High Risk"]
    else:
        prediction = ["Low Risk"]
    st.subheader("Prediction Result:")
    st.success(f"Risk Level: {prediction[0]}")

    if prediction[0] == "High Risk":
        st.error("⚠ Immediate medical consultation recommended!")
    elif prediction[0] == "Medium Risk":
        st.warning("Monitor health regularly and consult doctor.")
    else:
        st.info("Low Risk. Maintain healthy li.")
