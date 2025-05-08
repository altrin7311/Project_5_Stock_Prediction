import pandas as pd
import matplotlib.pyplot as plt

def plot_trend(csv_path="data/sp500_raw.csv"):
    # Skip the first 2 metadata rows
    df = pd.read_csv(csv_path, skiprows=2)

    # Rename columns properly
    df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

    # Parse date and set as index
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df.set_index("Date", inplace=True)

    # Plot the Close price
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='S&P 500 Close')
    plt.title("S&P 500 Close Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_trend()