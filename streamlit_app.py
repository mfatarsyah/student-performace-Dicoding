# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan encoder
model = joblib.load('student_status_model.joblib')
label_encoder = joblib.load('label_encoder.joblib')

# Judul aplikasi
st.title("🎓 Prediksi Dropout Mahasiswa - Jaya Jaya Institut")

st.markdown("Masukkan data berikut untuk memprediksi apakah mahasiswa akan Dropout, Enrolled, atau Graduate.")

# Input dari user
gender = st.selectbox("Jenis Kelamin", ['Laki-laki', 'Perempuan'])
displaced = st.selectbox("Apakah Mahasiswa Pengungsi?", ['Tidak', 'Ya'])
special_needs = st.selectbox("Memiliki Kebutuhan Khusus?", ['Tidak', 'Ya'])
debtor = st.selectbox("Memiliki Tunggakan?", ['Tidak', 'Ya'])
tuition_up_to_date = st.selectbox("Pembayaran Biaya Kuliah Tepat Waktu?", ['Tidak', 'Ya'])
scholarship_holder = st.selectbox("Penerima Beasiswa?", ['Tidak', 'Ya'])
international = st.selectbox("Mahasiswa Internasional?", ['Tidak', 'Ya'])

# Fitur numerik
age = st.number_input("Umur saat Pendaftaran", min_value=15, max_value=100, value=18)
curricular_units_1st_sem_grade = st.slider("Rata-rata Nilai Semester 1", 0.0, 20.0, 10.0)
curricular_units_2nd_sem_grade = st.slider("Rata-rata Nilai Semester 2", 0.0, 20.0, 10.0)

# Konversi ke format input model
input_data = {
    'Gender': 0 if gender == 'Laki-laki' else 1,
    'Displaced': 1 if displaced == 'Ya' else 0,
    'Educational_special_needs': 1 if special_needs == 'Ya' else 0,
    'Debtor': 1 if debtor == 'Ya' else 0,
    'Tuition_fees_up_to_date': 1 if tuition_up_to_date == 'Ya' else 0,
    'Scholarship_holder': 1 if scholarship_holder == 'Ya' else 0,
    'International': 1 if international == 'Ya' else 0,
    'Age_at_enrollment': age,
    'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
    'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade
}

input_df = pd.DataFrame([input_data])

# Load model
model = joblib.load('student_status_model.joblib')

# Prediksi
if st.button("Prediksi"):
    pred = model.predict(input_df)[0]
    label_map = {0: 'Graduate', 1: 'Enrolled', 2: 'Dropout'}
    st.success(f"📊 Hasil Prediksi: **{label_map[pred]}**")
