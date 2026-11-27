import streamlit as st
import joblib
import pandas as pd


# -------------------------------
# Load trained model
# -------------------------------
@st.cache_resource
def load_model():
    return joblib.load("car_price_model.pkl")

model = load_model()

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# -------------------------------
# Application UI
# -------------------------------
st.title("🚗 Used Car Price Predictor")

st.markdown(
    """
    Estimate the resale value of a used car using a machine learning model.

    Enter the car's details below to get an estimated resale price.
    """
)

st.divider()

# -------------------------------
# User inputs
# -------------------------------
name = st.text_input(
    "Car Name / Brand",
    placeholder="e.g. Maruti Swift"
)

location = st.selectbox(
    "Location",
    [
        "Mumbai", "Hyderabad", "Kochi", "Coimbatore",
        "Pune", "Delhi", "Chennai", "Jaipur",
        "Bangalore", "Ahmedabad", "Kolkata",
        "Lucknow", "Other"
    ]
)

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2026,
    value=2018
)

km = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=1000000,
    value=50000,
    step=1000
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner Type",
    ["First", "Second", "Third", "Fourth & Above"]
)

mileage = st.number_input(
    "Mileage (km/l)",
    min_value=0.0,
    max_value=100.0,
    value=18.0,
    step=0.1
)

engine = st.number_input(
    "Engine (CC)",
    min_value=0.0,
    max_value=10000.0,
    value=1200.0,
    step=100.0
)

power = st.number_input(
    "Power (bhp)",
    min_value=0.0,
    max_value=2000.0,
    value=80.0,
    step=1.0
)

seats = st.selectbox(
    "Number of Seats",
    [2, 4, 5, 6, 7, 8, 9, 10],
    index=2
)

st.divider()

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Car Price", use_container_width=True):

    if not name.strip():
        st.warning("Please enter a car name.")
    else:

        # Convert full car name into brand
        name = name.strip().split()[0]

        # Create input dataframe
        input_data = pd.DataFrame([{
            "Name": name,
            "Location": location,
            "Year": year,
            "Kilometers_Driven": km,
            "Fuel_Type": fuel,
            "Transmission": transmission,
            "Owner_Type": owner,
            "Mileage": mileage,
            "Engine": engine,
            "Power": power,
            "Seats": seats
        }])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Display result
        st.success(
            f"Estimated Resale Price: ₹{prediction:.2f} Lakhs"
        )

        st.caption(
            "This is a machine learning estimate and not an actual market quotation."
        )

