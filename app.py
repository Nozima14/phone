import streamlit as st
import pickle
import numpy as np

# Load the model
with open("telefonmodel.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Telefon Narxini Bashorat Qilish")

# Input form
st.header("Telefon parametrlarini kiriting")
sale = st.slider("Sale (%)", min_value=0, max_value=100, value=10)
weight = st.slider("Og'irlik (g)", min_value=50, max_value=500, value=150)
resoloution = st.selectbox("Ekran Ruxsatnomasi", options=[720, 1080, 1440, 2160])
ppi = st.slider("PPI", min_value=100, max_value=600, value=300)
cpu_core = st.slider("CPU Yadrolar soni", min_value=1, max_value=16, value=8)
cpu_freq = st.slider("CPU Chastotasi (GHz)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)
internal_mem = st.slider("Ichki Xotira (GB)", min_value=8, max_value=1024, value=128)
ram = st.slider("RAM (GB)", min_value=1, max_value=64, value=8)
rear_cam = st.slider("Orqa Kamera (MP)", min_value=2, max_value=200, value=50)
front_cam = st.slider("Old Kamera (MP)", min_value=2, max_value=40, value=12)
battery = st.slider("Batareya sig'imi (mAh)", min_value=1000, max_value=8000, value=4000)
thickness = st.slider("Qalinlik (mm)", min_value=4.0, max_value=12.0, value=7.5, step=0.1)
lifespan = st.slider("Yaroqlilik muddati (yil)", min_value=1, max_value=10, value=5)
year = st.slider("Ishlab chiqarilgan yili", min_value=2010, max_value=2025, value=2020)
condition = st.selectbox("Telefon holati", options=["yangi", "ishlatilgan", "ta'mirlangan"])

# Map categorical data
condition_map = {"yangi": 1, "ishlatilgan": 0.5, "ta'mirlangan": 0.3}
condition_value = condition_map[condition]

# Bashorat tugmasi
if st.button("Bashorat qilish"):
    # Make prediction
    features = np.array([[sale, weight, resoloution, ppi, cpu_core, cpu_freq, internal_mem,
                          ram, rear_cam, front_cam, battery, thickness, lifespan, year, condition_value]])
    predicted_price = model.predict(features)

    st.subheader(f"Telefon Narxi Bashorati: {predicted_price[0]:,.2f} dollar")
