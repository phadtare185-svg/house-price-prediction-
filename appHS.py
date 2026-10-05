import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open(r"C:\Users\phadt\OneDrive\Desktop\MLproj\House price ML project(regression)\forest_reg.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

st.write("Enter the house details below to predict the price:")

# Replace these with your actual 8 features used in training
sqft = st.number_input("Square Footage", min_value=500, max_value=10000, step=50)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
year_built = st.number_input("Year Built", min_value=1900, max_value=2025, step=1)
garage = st.number_input("Garage Size (cars)", min_value=0, max_value=5, step=1)
lot_size = st.number_input("Lot Size (sqft)", min_value=100, max_value=20000, step=100)
floors = st.number_input("Number of Floors", min_value=1, max_value=5, step=1)
location_score = st.slider("Location Score (1-10)", min_value=1, max_value=10, step=1)

# Collect inputs into array (order must match training data!)
features = np.array([[sqft, bedrooms, bathrooms, year_built,
                      garage, lot_size, floors, location_score]])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")