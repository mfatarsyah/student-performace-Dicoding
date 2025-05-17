import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import time
from data_preprocessing import data_preprocessing

from data_preprocessing import (
    encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced,
    encoder_Gender, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date,
    scaler_Admission_grade, scaler_Curricular_units_1st_sem_approved,
    scaler_Curricular_units_1st_sem_credited, scaler_Curricular_units_1st_sem_enrolled,
    scaler_Curricular_units_1st_sem_grade, scaler_Curricular_units_2nd_sem_approved,
    scaler_Curricular_units_2nd_sem_credited, scaler_Curricular_units_2nd_sem_enrolled,
    scaler_Curricular_units_2nd_sem_grade, scaler_Previous_qualification_grade
)
from prediction import prediction

st.title("🎓 Student DropOut Prediction - Jaya Jaya Institute")
st.markdown("Enter the following data to predict whether a student will Dropout or Graduate")

data = {}

def encode_binary(label, encoder):
    user_input = st.selectbox(f"{label} (Yes/No)", ["Yes", "No"], index=1 if label == "Debtor" else 0)
    mapped_value = 1 if user_input == "Yes" else 0
    encoder.fit([0, 1])
    data[label] = [encoder.transform([mapped_value])[0]]

def create_slider(label, min_value, max_value, value):
    data[label] = [st.slider(label.replace('_', ' '), min_value=min_value, max_value=max_value, value=value)]

# Input form - vertically aligned
encode_binary("Tuition fees", encoder_Tuition_fees_up_to_date)
encode_binary("Scholarship holder", encoder_Scholarship_holder)
encode_binary("Debtor", encoder_Debtor)
encode_binary("Displaced", encoder_Displaced)
encode_binary("Daytime evening attendance", encoder_Daytime_evening_attendance)

Gender = st.selectbox("Gender", ["Female", "Male"], index=1)
encoder_Gender = LabelEncoder()
encoder_Gender.fit(["Female", "Male"])
data["Gender"] = encoder_Gender.transform([Gender])[0]

create_slider('Admission_grade', 95, 190, 100)
create_slider('Previous_qualification_grade', 95, 190, 100)

create_slider('Curricular_units_1st_sem_approved', 0, 26, 5)
create_slider('Curricular_units_1st_sem_grade', 0, 18, 5)
create_slider('Curricular_units_1st_sem_enrolled', 0, 26, 5)
create_slider('Curricular_units_1st_sem_credited', 0, 20, 5)

create_slider('Curricular_units_2nd_sem_approved', 0, 20, 5)
create_slider('Curricular_units_2nd_sem_grade', 0, 20, 12)
create_slider('Curricular_units_2nd_sem_enrolled', 0, 23, 5)
create_slider('Curricular_units_2nd_sem_credited', 0, 19, 5)

# Prediction
if st.button('Click Here to Predict'):
    new_data = data_preprocessing(data=data)
    with st.spinner('Predicting...'):
        time.sleep(2)
        output = prediction(new_data)
        st.success(f"Prediction: {output}")
