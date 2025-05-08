# app/plot_utils.py
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_price_forecast(predicted_close):
    df = pd.read_csv("data/sp500_features.csv", parse_dates=["Date"])
    df.set_index("Date", inplace=True)

    fig, ax = plt.subplots()
    df["Close"].plot(ax=ax, color="black", linewidth=2, label="Close Price")
    ax.axhline(y=predicted_close, color="green", linestyle="--", label="Predicted Close")
    ax.set_title("S&P 500 Price with Forecast")
    ax.legend()
    st.pyplot(fig)