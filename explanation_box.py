# app/explanation_box.py
import streamlit as st

def display_reasoning(forecast):
    st.markdown("### 🧠 Reasoning Behind Prediction")
    
    st.markdown("#### 📰 News Summary")
    st.info(forecast["news_summary"])

    st.markdown("#### 📊 Technical Analysis")
    for item in forecast["interpretation"]:
        st.write(f"- {item}")