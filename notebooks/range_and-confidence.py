import pandas as pd
import numpy as np
import tensorflow as tf
from datetime import timedelta
from pandas.tseries.holiday import USFederalHolidayCalendar

def predict_range_and_confidence(
    model_path="models/lstm_direction_model.h5",
    data_path="data/sp500_features.csv",
    time_steps=10,
    threshold=0.6
):
    # Load the trained model
    model = tf.keras.models.load_model(model_path)

    # Load and prepare the feature dataset
    df = pd.read_csv(data_path, parse_dates=["Date"], index_col="Date")
    features = ["Close", "Returns", "EMA_21", "RSI_14", "ATR_14"]

    # Get the last `time_steps` rows
    recent_data = df[-(time_steps + 1):]
    X_input = recent_data[features].values[:-1]  # exclude the target day

    # Reshape input
    X_input = np.expand_dims(X_input, axis=0)

    # Predict direction
    pred = model.predict(X_input)[0][0]
    direction = "Up" if pred >= 0.5 else "Down"
    confidence = round(float(pred if direction == "Up" else 1 - pred), 4)

    # Range calculation
    last_close = recent_data["Close"].values[-2]
    last_atr = recent_data["ATR_14"].values[-2]
    predicted_range = (round(last_close - last_atr, 2), round(last_close + last_atr, 2))

    # Forecast date (next trading day)
    def get_next_trading_day(current_date):
        cal = USFederalHolidayCalendar()
        holidays = cal.holidays(start=current_date, end=current_date + timedelta(days=10))
        next_day = current_date + timedelta(days=1)
        while next_day.weekday() >= 5 or next_day in holidays:
            next_day += timedelta(days=1)
        return next_day

    forecast_date = get_next_trading_day(df.index[-1].date())

    # Decision logic
    decision = "🔼 Buy" if direction == "Up" and confidence >= threshold else \
               "🔽 Sell" if direction == "Down" and confidence >= threshold else \
               "⚠️ No Trade – Low Confidence"

    # Final output
    print(f"📅 Date: {forecast_date}")
    print(f"📈 Direction: {direction}")
    print(f"📊 Predicted Range: {predicted_range[0]} to {predicted_range[1]}")
    print(f"🎯 Confidence: {confidence}")
    print(f"💡 Decision: {decision}")

# Run if this file is executed directly
if __name__ == "__main__":
    predict_range_and_confidence()