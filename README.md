# 📈 S&P 500 Forecast using LSTM
<img width="377" alt="Screenshot 2025-05-08 at 9 27 24 PM" src="https://github.com/user-attachments/assets/407a8738-c315-48cd-8060-8971b2a98228" />
<img width="377" alt="Screenshot 2025-05-08 at 9 27 30 PM" src="https://github.com/user-attachments/assets/afb12197-4923-44f3-af62-da56a0e254a7" />



An LSTM powered dashboard that forecasts the **next-day S&P 500 closing price** using a hybrid system of technical indicators, news sentiment, and deep learning (LSTM). Built with **Streamlit**, this project combines ML intelligence and market reasoning in a single, intuitive interface.

---

## 🧠 Features

- 🔍 **LSTM Forecasting**: Predicts market direction and expected movement percentage.
- 📰 **News Agent**: Automatically retrieves recent S&P 500-related headlines.
- 📊 **Technical Agent**: Calculates indicators like RSI, EMA, MACD, OBV, ATR, Bollinger Bands, etc.
- 🧾 **Final Decision Agent**: Merges signals from news and technicals to predict the next day's close.
- 📈 **Stocks-style Plot**: Visualizes price forecast in a familiar interface.
- 📦 Modular codebase with explainable outputs.

---

## 🗂️ Project Structure (Not how it is in the repo)

```
Project_5_Stock_Prediction/
├── app/                     # Streamlit frontend
│   ├── app.py               # Main dashboard script
│   ├── forecast_engine.py   # Runs full pipeline
│   ├── forecast_card.py     # Displays forecast result box
│   ├── explanation_box.py   # Shows reasoning behind the forecast
│   ├── plot_utils.py        # iOS-style chart visuals
│   └── style.css            # Custom styling
│
├── agents/                  # Backend intelligence
│   ├── news_agent.py        # News collection agent
│   ├── technical_agent.py   # Indicator analyzer
│   └── final_decision_agent.py # Combines all outputs
│
├── data/
│   ├── sp500_raw.csv        # Raw S&P 500 historical data
│   └── sp500_features.csv   # Feature-engineered data
│
├── models/                  # Trained LSTM model
│   └── lstm_direction_model.h5
│
├── notebooks/               # Experiment notebooks
├── outputs/                 # Any generated plots or exports
├── requirements.txt         # Dependencies
└── .gitignore
```

---

## 🧪 How It Works

### 1. **Technical Agent**
- Reads `sp500_features.csv`
- Computes indicators:
  - RSI (14), EMA (21), MACD, MACD Signal
  - ATR (14), OBV, Bollinger Bands
- Generates market interpretation like "RSI indicates overbought", etc.

### 2. **News Agent**
- Fetches recent headlines via [NewsAPI](https://newsapi.org/)
- Displays top 3 stories and their metadata

### 3. **LSTM Model**
- Trained on closing prices
- Predicts **direction** and **expected movement (%)**

### 4. **Final Decision Agent**
- Merges LSTM + technical + news sentiment
- Outputs final forecast:
  - `Direction`, `Confidence`, `Expected % Move`, `Predicted Close`

---

## 🖥️ Run Locally

```bash
# Clone the repo
git clone https://github.com/altrin7311/sp500-forecast-app.git
cd sp500-forecast-app

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # (use venv\Scripts\activate on Windows)

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app/app.py
```

---

## 🔐 API Key

To use the News Agent:
1. Create an account at [https://newsapi.org](https://newsapi.org)
2. Replace `your_default_key_here` in `news_agent.py` with your API key

---

## 📌 Requirements

- Python 3.8+
- TensorFlow 
- yfinance
- pandas, numpy, matplotlib, scikit-learn
- Streamlit

---

## 🚀 Deployment (Optional)

To deploy on **Streamlit Cloud**:
1. Push this repo to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Link your GitHub account
4. Deploy directly with `app/app.py` as the main script

---

## 📄 License

MIT License. Feel free to use and modify this project for academic, personal, or commercial purposes.

---

## 🙋‍♂️ Author

Built with ❤️ by [Altrin Titus](https://www.linkedin.com/in/altrin-titus-101443293)
