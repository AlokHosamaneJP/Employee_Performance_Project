# X order -> 'Years_At_Company', 'Monthly_Salary', 'Overtime_Hours', 'Promotions','Employee_Satisfaction_Score'
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl

import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Employee Performance Prediction")

st.divider()

st.write("You can get employee performance after entering values")

st.divider()

years = st.number_input("Enter the years at company",min_value=0, max_value=20, value = 2)
salary = st.number_input("Enter monthly salary", min_value=1000, max_value= 10000, value = 5000)
overtime = st.number_input("Enter overtime hours", min_value= 0, max_value=100, value = 0)
promotions = st.number_input("Enter promotions",min_value= 0, max_value= 10, value = 0)
satisfaction = st.number_input("Enter employee satifaction", min_value = 0.0, max_value = 5.0, value=2.0)

X = [years, salary,overtime, promotions, satisfaction]

st.divider()

predictionbutton = st.button("Predict performance score")

st.divider()

if predictionbutton:
    X1 = np.array(X)
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]
    st.write(f"Prediction for the performance score is {prediction}")



else:
    st.write("Please use the button for prediction") 