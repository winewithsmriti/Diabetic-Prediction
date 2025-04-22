import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sqlite3
import os

# --- Load model and scaler ---
assert os.path.exists("diabetes_model.pkl"), "❌ Model file not found!"
assert os.path.exists("scaler.pkl"), "❌ Scaler file not found!"

model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# --- Database connection ---
def connect_db():
    return sqlite3.connect('diabetes_prediction.db')

# --- Create table if it doesn't exist ---
def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            pregnancies INTEGER,
            glucose INTEGER,
            blood_pressure INTEGER,
            skin_thickness INTEGER,
            insulin INTEGER,
            bmi REAL,
            dpf REAL,
            age INTEGER,
            prediction_result TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

# --- Insert patient prediction into database ---
def insert_patient_data(patient_name, pregnancies, glucose, bp, skin, insulin, bmi, dpf, age, prediction_result):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO predictions (patient_name, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age, prediction_result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (patient_name, pregnancies, glucose, bp, skin, insulin, bmi, dpf, age, prediction_result))
    conn.commit()
    conn.close()

# --- Streamlit Page Config ---
st.set_page_config(page_title="Diabetes Predictor", layout="centered")

# --- Styling ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f0f8ff, #e6f7ff);
        padding: 20px;
    }
    h1 {
        color: #004080;
        text-align: center;
    }
    .stButton>button {
        background-color: #add8e6;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    .stTextInput input, .stNumberInput input {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #add8e6;
        padding: 10px;
        font-size: 16px;
    }
    .stSuccess {
        background-color: #90ee90;
        color: black;
        padding: 15px;
        border-radius: 8px;
        font-size: 18px;
    }
    .stError {
        background-color: #f8d7da;
        color: black;
        padding: 15px;
        border-radius: 8px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("🩺 Diabetes Prediction Web App")

# --- Input Section ---
patient_name = st.text_input("Patient Name", "")
st.markdown("Fill in the following health details to predict if the person is diabetic:")

col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose Level", 0, 200, 100)
    bp = st.number_input("Blood Pressure", 0, 150, 70)
    skin = st.number_input("Skin Thickness", 0, 100, 20)

with col2:
    insulin = st.number_input("Insulin Level", 0, 900, 80)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0, step=0.1)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5, step=0.01)
    age = st.number_input("Age", 0, 120, 30)

# --- Predict Button ---
if st.button("Predict"):
    if patient_name.strip():
        input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        # Show prediction
        st.markdown("---")
        st.subheader(f"🔍 Prediction Result for {patient_name}")
        result = "🟥 Diabetic" if prediction == 1 else "🟩 Not Diabetic"
        st.success(f"The person is predicted to be: **{result}**")

        # Save to database
        insert_patient_data(patient_name, pregnancies, glucose, bp, skin, insulin, bmi, dpf, age, result)

        # Show summary
        st.markdown("---")
        st.subheader("📊 Input Summary")
        columns = ["Patient Name", "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DPF", "Age", "Prediction Result"]
        df_input = pd.DataFrame([[patient_name] + list(input_data[0]) + [result]], columns=columns)
        st.table(df_input)
    else:
        st.error("Please enter the patient's name.")

# --- Footer ---
st.markdown("---")
st.markdown("<center><small>Made with ❤️ using Streamlit | © 2025</small></center>", unsafe_allow_html=True)
