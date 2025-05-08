# app/forecast_card.py
import streamlit as st

def display_forecast_card(forecast):
    st.markdown("### 🎯 Forecast Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Direction", forecast["direction"])
    col2.metric("Expected Move (%)", forecast["expected_move_percent"])
    col3.metric("Predicted Close", round(forecast["predicted_close"], 2))