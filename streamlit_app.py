#Students_Performance.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from PIL import Image
import time
from data_preprocessing import data_preprocessing

from data_preprocessing import encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced, encoder_Gender, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date
from data_preprocessing import scaler_Admission_grade, scaler_Curricular_units_1st_sem_approved, scaler_Curricular_units_1st_sem_credited, scaler_Curricular_units_1st_sem_enrolled, scaler_Curricular_units_1st_sem_grade, scaler_Curricular_units_2nd_sem_approved, scaler_Curricular_units_2nd_sem_credited, scaler_Curricular_units_2nd_sem_enrolled, scaler_Curricular_units_2nd_sem_grade, scaler_Previous_qualification_grade

from prediction import prediction

# Judul aplikasi
st.title("🎓 Prediksi Dropout Mahasiswa - Jaya Jaya Institut")

st.markdown("Masukkan data berikut untuk memprediksi apakah mahasiswa akan Dropout, Enrolled, atau Graduate.")

# Initialize an empty dictionary to store user input
data = {}

# Convert user input dictionary to DataFrame
user_input_df = pd.DataFrame(data, index=[0])

# Helper functions
def encode_selection(encoder, selection, labels):
    encoder.fit(labels)
    return encoder.transform([selection])[0]

def create_slider(label, min_value, max_value, default):
    data[label] = [st.slider(label.replace('_', ' '), min_value, max_value, default)]

# Form Input
st.markdown("### Input Student Data Below")

# Binary Selections
st.markdown("#### Student Status")
data['Tuition_fees_up_to_date'] = [encoder_Tuition_fees_up_to_date.fit_transform([st.selectbox("Tuition fees up to date", [0, 1])])[0]]
data['Scholarship_holder'] = [encoder_Scholarship_holder.fit_transform([st.selectbox("Scholarship holder", [0, 1])])[0]]
data['Debtor'] = [encoder_Debtor.fit_transform([st.selectbox("Debtor", [0, 1])])[0]]
data['Displaced'] = [encoder_Displaced.fit_transform([st.selectbox("Displaced", [0, 1])])[0]]
data['Daytime_evening_attendance'] = [encoder_Daytime_evening_attendance.fit_transform([st.selectbox("Attendance (Daytime/Evening)", [0, 1])])[0]]

# Gender
st.markdown("#### Demographics")
encoder_Gender = LabelEncoder()
encoder_Gender.fit(["Female", "Male"])
gender = st.selectbox("Gender", ["Female", "Male"])
data['Gender'] = encoder_Gender.transform([gender])[0]

# Grade Inputs
st.markdown("#### Grades and Academic Units")
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

# Display raw input
st.markdown("### Review Your Input")
user_input_df = pd.DataFrame(data)
st.dataframe(user_input_df, use_container_width=True)

# Prediction
if st.button("Click Here to Predict"):
    with st.spinner("Processing..."):
        time.sleep(2)
        preprocessed_data = data_preprocessing(data)
        result = prediction(preprocessed_data)
        st.success(f"Prediction: {result}")
