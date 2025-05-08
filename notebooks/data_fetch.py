import yfinance as yf
import pandas as pd
from datetime import date
import os

def fetch_sp500_data(start="2010-01-01", save_path="data/sp500_raw.csv"):
    # Always use today's date as end
    end = date.today().strftime("%Y-%m-%d")

    print(f"📡 Fetching S&P 500 data from {start} to {end}...")
    df = yf.download("^GSPC", start=start, end=end, interval="1d", auto_adjust=True, progress=False)

    # Reset and save
    df.reset_index(inplace=True)
    os.makedirs("data", exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"✅ Data saved to: {save_path}")
    print(df.tail(3))  # show the last few rows to confirm freshness

if __name__ == "__main__":
    fetch_sp500_data()
import yfinance as yf
import pandas as pd
from datetime import date
import os

def fetch_sp500_data(start="2010-01-01", save_path="data/sp500_raw.csv"):
    # Always use today's date as end
    end = date.today().strftime("%Y-%m-%d")

    print(f"📡 Fetching S&P 500 data from {start} to {end}...")

    try:
        df = yf.download(
            "^GSPC",
            start=start,
            end=end,
            interval="1d",
            auto_adjust=True,
            progress=True,
            show_errors=True,
        )

        if df.empty:
            print("⚠️ No data was fetched. Check if the date range includes a market holiday or weekend.")
            return

        # Reset index and save
        df.reset_index(inplace=True)
        os.makedirs("data", exist_ok=True)
        df.to_csv(save_path, index=False)
        print(f"✅ Data saved to: {save_path}")
        print(df.tail(3))  # show the last few rows to confirm freshness

    except Exception as e:
        print(f"❌ Error occurred while fetching data: {e}")

if __name__ == "__main__":
    fetch_sp500_data()