import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import os
from tensorflow.keras.callbacks import EarlyStopping

physical_devices = tf.config.list_physical_devices('GPU')
print("🖥️ Available GPUs:", physical_devices)
if physical_devices:
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print("✅ GPU memory growth enabled")
    except:
        print("⚠️ Could not set memory growth on GPU")
else:
    print("⚠️ No GPU available, using CPU instead")

def load_data(path="data/sp500_features.csv", time_steps=10):
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")

    features = ["Close", "Returns", "EMA_21", "RSI_14", "ATR_14"]
    target_col = "Target"

    # Normalize features
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(df[features])

    X, y = [], []
    for i in range(time_steps, len(df)):
        X.append(scaled_features[i - time_steps:i])
        y.append(df[target_col].iloc[i])

    return np.array(X), np.array(y)

def build_model(input_shape):
    model = Sequential([
        LSTM(64, return_sequences=False, input_shape=input_shape),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_and_save_model():
    tf.random.set_seed(42)
    np.random.seed(42)
    print("📥 Loading data...")
    X, y = load_data()
    print(f"🧠 Training on {len(X)} samples...")

    model = build_model(input_shape=(X.shape[1], X.shape[2]))

    epochs = 40
    batch_size = 32
    early_stopping = EarlyStopping(monitor='loss', patience=3, restore_best_weights=True)
    for epoch in range(epochs):
        print(f"\n🚀 Epoch {epoch+1}/{epochs}")
        print("📊 Training on device:", "/GPU:0" if physical_devices else "/CPU:0")
        history = model.fit(X, y, batch_size=batch_size, epochs=1, verbose=1, callbacks=[early_stopping])

    print("🏁 Training complete.")
    os.makedirs("models", exist_ok=True)
    model.save("models/lstm_direction_model.h5")
    print("\n✅ Model saved to models/lstm_direction_model.h5")

if __name__ == "__main__":
    train_and_save_model()