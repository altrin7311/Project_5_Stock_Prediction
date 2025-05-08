import pandas as pd
from news_agent import fetch_sp500_news 
from technical_agent import analyze_technical_signals

def make_final_prediction(raw_data_path="data/sp500_raw.csv"):
    # Load raw data and get latest close
    df = pd.read_csv(raw_data_path, parse_dates=["Date"])
    df.sort_values("Date", inplace=True)
    # Remove any rows where 'Close' is not a number (e.g., symbols like ^GSPC)
    df = df[pd.to_numeric(df["Close"], errors="coerce").notnull()]
    latest_close = float(df["Close"].iloc[-1])
    
    # Get news and technical analysis
    news_articles = fetch_sp500_news()
    if isinstance(news_articles, list) and len(news_articles) > 0:
        titles = [article["title"] for article in news_articles if "title" in article]
        summary = "\n".join(titles[:3])
        sentiment = "Neutral"  # Placeholder until sentiment analysis is added
    else:
        summary = "No articles available."
        sentiment = "Neutral"

    tech_output = analyze_technical_signals()

    # Apply sentiment weight
    sentiment_factor = 1.0

    if sentiment == "Positive":
        sentiment_factor += 0.02
    elif sentiment == "Negative":
        sentiment_factor -= 0.02

    # Final expected move (percent)
    expected_percent = tech_output["expected_move"] * sentiment_factor

    # Direction (from EMA crossover or MACD)
    direction = "Up" if "bullish" in " ".join(tech_output["interpretation"]).lower() else "Down"

    # Predict tomorrow's closing rate
    if direction == "Up":
        predicted_close = latest_close * (1 + expected_percent / 100)
    else:
        predicted_close = latest_close * (1 - expected_percent / 100)

    return {
        "today_close": round(latest_close, 2),
        "predicted_close": round(predicted_close, 2),
        "expected_move_percent": round(expected_percent, 2),
        "direction": direction,
        "news_sentiment": sentiment,
        "news_summary": summary,
        "indicators": tech_output["indicators"],
        "interpretation": tech_output["interpretation"]
    }

# ✅ Test run
if __name__ == "__main__":
    forecast = make_final_prediction()
    print("\n📊 FINAL FORECAST:")
    for k, v in forecast.items():
        print(f"{k}: {v}")