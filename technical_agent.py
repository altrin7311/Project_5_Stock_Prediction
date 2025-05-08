import pandas as pd
import numpy as np

def analyze_technical_signals(feature_csv="data/sp500_features.csv"):
    print("🔍 Loading data...")

    # Load the feature data
    df = pd.read_csv(feature_csv)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    latest = df.iloc[-1]

    # Extract indicator values
    indicators = {
        "Close": round(latest["Close"], 2),
        "Open": round(latest["Open"], 2),
        "High": round(latest["High"], 2),
        "Low": round(latest["Low"], 2),
        "Volume": round(latest["Volume"], 2),
        "Returns": round(latest["Returns"], 4),
        "RSI_14": round(latest["RSI_14"], 2),
        "EMA_21": round(latest["EMA_21"], 2),
        "ATR_14": round(latest["ATR_14"], 2),
        "MACD": round(latest["MACD"], 4),
        "MACD_Signal": round(latest["MACD_Signal"], 4),
        "OBV": round(latest["OBV"], 2),
        "BB_Upper": round(latest["BB_Upper"], 2),
        "BB_Lower": round(latest["BB_Lower"], 2),
    }

    print("🧠 Interpreting indicators...")
    interpretation = []

    if indicators["RSI_14"] > 70:
        interpretation.append("RSI indicates overbought conditions")
    elif indicators["RSI_14"] < 30:
        interpretation.append("RSI indicates oversold conditions")
    else:
        interpretation.append("RSI is neutral")

    if indicators["Close"] > indicators["EMA_21"]:
        interpretation.append("Price is above EMA (uptrend)")
    else:
        interpretation.append("Price is below EMA (downtrend)")

    if indicators["ATR_14"] > 0.03 * indicators["Close"]:
        interpretation.append("High volatility detected (ATR > 3% of Close)")
    else:
        interpretation.append("Volatility is moderate")

    if indicators["MACD"] > indicators["MACD_Signal"]:
        interpretation.append("MACD crossover indicates potential bullish momentum")
    else:
        interpretation.append("MACD crossover suggests bearish sentiment")

    # 🔢 Compute expected percentage move based on ATR and MACD relative to price
    atr_percent = (indicators["ATR_14"] / indicators["Close"]) * 100
    macd_percent = ((indicators["MACD"] - indicators["MACD_Signal"]) / indicators["Close"]) * 100
    expected_move = round(abs(atr_percent + macd_percent), 2)

    

    return {
        
        "indicators": indicators,
        "interpretation": interpretation,
        "expected_move": expected_move
    }

# ✅ Test run
if __name__ == "__main__":
    output = analyze_technical_signals()
    print("\n📊 Technical Indicator Output:")
    print(output)