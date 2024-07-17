

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Define the layout
def main():
    st.title("Car Price Prediction")

    # Sidebar
    st.sidebar.title("Input Features")

    # Input fields
    name = st.sidebar.text_input("Car Name", "")
    company = st.sidebar.text_input("Company", "")
    year = st.sidebar.number_input("Year", 1885, 2024, 2022)
    kms_driven = st.sidebar.number_input("Kilometers Driven", 0, 1000000, 0)
    fuel_type = st.sidebar.selectbox("Fuel Type", ['Petrol', 'Diesel', 'LPG'])

    # Make prediction
    input_data = pd.DataFrame({'name': [name], 'company': [company], 'year': [year],
                               'kms_driven': [kms_driven], 'fuel_type': [fuel_type]})
    if st.sidebar.button("Predict"):
        prediction = predict_price(input_data)
        if prediction >= 0:
            st.sidebar.subheader("Predicted Price")
            st.sidebar.write(f"Rs. {prediction:.2f}")
        else:
            st.sidebar.error("Error: Negative Price Prediction")

# Function to make prediction
def predict_price(input_df):
    prediction = model.predict(input_df)[0]
    return max(0, prediction)  # Ensure predicted price is non-negative

if __name__ == "__main__":
    main()

