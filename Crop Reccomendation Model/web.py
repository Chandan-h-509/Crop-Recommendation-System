import streamlit as st
import requests

# Define the FastAPI server URL
fastapi_url = "http://127.0.0.1:8000/predict"

st.title("Crop Prediction App")
st.markdown("Welcome to the Crop Prediction App. This app helps you predict the best crop to grow based on various environmental parameters. Simply enter the input parameters, and we will provide you with a crop recommendation.")

st.sidebar.header("Input Parameters")

N = st.sidebar.number_input("N", min_value=0.0, max_value=200.0, value=100.0)
P = st.sidebar.number_input("P", min_value=0.0, max_value=200.0, value=40.0)
K = st.sidebar.number_input("K", min_value=0.0, max_value=200.0, value=50.0)
temperature = st.sidebar.number_input("Temperature", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.sidebar.number_input("Humidity", min_value=0.0, max_value=100.0, value=60.0)
ph = st.sidebar.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.sidebar.number_input("Rainfall", min_value=0.0, max_value=1000.0, value=100.0)

if st.button("Predict"):
    payload = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    response = requests.post(fastapi_url, json=payload)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted Crop: {prediction}")
    else:
        st.error("Error in making the prediction")

# uvicorn main:app --reload
# streamlit run web.py
