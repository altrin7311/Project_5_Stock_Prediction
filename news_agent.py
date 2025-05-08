import requests
import datetime
import os

def fetch_sp500_news(api_key=None, query="S&P 500", max_articles=5):
    """
    Fetch top headlines related to the S&P 500 from NewsAPI.
    Returns a summary of article titles and source metadata.
    """
    if api_key is None:
        api_key = os.getenv("NEWS_API_KEY", "your_default_key_here")
    url = "https://newsapi.org/v2/everything"
    today = datetime.date.today().isoformat()
    params = {
        "q": query,
        "from": today,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": api_key,
        "pageSize": max_articles
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])

        print(f"📰 Retrieved {len(articles)} S&P 500-related news articles for {today}.")

        output = []
        for article in articles:
            output.append({
                "title": article["title"],
                "source": article["source"]["name"],
                "published": article["publishedAt"],
                "summary": article.get("description", "")
            })

        return output

    except Exception as e:
        print("❌ Failed to fetch news:", e)
        return []

# Test the agent
if __name__ == "__main__":
    YOUR_API_KEY = "c011934aa3ce446bb1ed744288458ece"
    news_data = fetch_sp500_news(YOUR_API_KEY)
    for i, article in enumerate(news_data, 1):
        print(f"\n{i}. 🗞️ {article['title']}")
        print(f"   🏢 Source: {article['source']}")
        print(f"   📅 Published: {article['published']}")
        print(f"   📌 Summary: {article['summary']}")