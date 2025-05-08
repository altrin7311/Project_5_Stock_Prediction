# app/app.py
import streamlit as st
from forecast_engine import run_forecast
from forecast_card import display_forecast_card
from plot_utils import plot_price_forecast
from explanation_box import display_reasoning

st.set_page_config(page_title="S&P 500 AI Forecast", layout="wide")
st.markdown('<style>' + open("style.css").read() + '</style>', unsafe_allow_html=True)

st.title("📈 S&P 500 AI Forecast Dashboard")

forecast = run_forecast()
display_forecast_card(forecast)
plot_price_forecast(forecast["predicted_close"])
display_reasoning(forecast)