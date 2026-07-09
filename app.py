import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Rising Waters",
    page_icon="🌊",
    layout="wide"
)

# Bright background and custom styling
st.markdown("""
<style>
.stApp {
    background-color: #87CEFA;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #E0F7FF, #87CEFA);
}
</style>
""", unsafe_allow_html=True)



# Load trained model
model = joblib.load("model.pkl")

# Title
st.markdown("<h1>🌊 Rising Waters</h1>", unsafe_allow_html=True)
st.markdown("<h3>Flood Risk Prediction System</h3>", unsafe_allow_html=True)

# Information box
st.info("Enter the environmental values below to predict the flood risk level.")

# Input fields in two columns
col1, col2 = st.columns(2)

with col1:
    rainfall = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=0.0,
        value=0.0
    )

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=0.0,
        value=0.0
    )

with col2:
    river_level = st.number_input(
        "🌊 River Level (m)",
        min_value=0.0,
        value=0.0
    )

    humidity = st.number_input(
        "💧 Humidity (%)",
        min_value=0.0,
        value=0.0
    )

st.write("")

# Prediction button
if st.button("📊 Predict Flood Risk"):

    prediction = model.predict(
        [[rainfall, river_level, temperature, humidity]]
    )

    if prediction[0] == "High":
        st.error("🔴 Flood Risk: HIGH")

    elif prediction[0] == "Medium":
        st.warning("🟡 Flood Risk: MEDIUM")

    else:
        st.success("🟢 Flood Risk: LOW")

st.markdown("---")
st.markdown(
    "<center>Developed by Divija | B.Tech CSE (AI & ML)</center>",
    unsafe_allow_html=True
)
