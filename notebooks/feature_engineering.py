import pandas as pd
import numpy as np

def add_technical_indicators(df):
    # RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / (avg_loss + 1e-6)
    df['RSI_14'] = 100 - (100 / (1 + rs))

    # EMA (Exponential Moving Average)
    df['EMA_21'] = df['Close'].ewm(span=21, adjust=False).mean()

    # ATR (Average True Range)
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df['ATR_14'] = tr.rolling(window=14).mean()

    # MACD and MACD Signal
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

    # On-Balance Volume (OBV)
    df['OBV'] = (np.sign(df['Close'].diff()) * df['Volume']).fillna(0).cumsum()

    # Bollinger Bands
    sma_20 = df['Close'].rolling(window=20).mean()
    std_20 = df['Close'].rolling(window=20).std()
    df['BB_Upper'] = sma_20 + (2 * std_20)
    df['BB_Lower'] = sma_20 - (2 * std_20)

    return df

def engineer_features(csv_path="data/sp500_raw.csv", output_path="data/sp500_features.csv"):
    # Load data and skip the 2 metadata rows
    df = pd.read_csv(csv_path, skiprows=2)
    df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

    # Parse and set index
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df.set_index("Date", inplace=True)

    # Calculate returns
    df["Returns"] = df["Close"].pct_change()

    # Add technical indicators
    df = add_technical_indicators(df)

    # Create target label for direction: 1 if next day's close is higher
    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    # Drop rows with NaNs
    df.dropna(inplace=True)

    # Save feature-enhanced CSV
    df.to_csv(output_path)
    print(f"✅ Feature-enhanced dataset saved to: {output_path}")
    print(df[["Close", "Returns", "EMA_21", "RSI_14", "ATR_14", "MACD", "MACD_Signal", "OBV", "BB_Upper", "BB_Lower", "Target"]].tail())

if __name__ == "__main__":
    engineer_features()