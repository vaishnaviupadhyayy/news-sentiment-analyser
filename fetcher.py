import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY= os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
def fetch_headlines(topic: str, count: int = 20) -> list[dict]:
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": count,
        "apiKey": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    return [
        {
            "title": a["title"],
            "source": a["source"]["name"],
            "published": a["publishedAt"][:10],
            "url": a["url"],
        }
        for a in articles
        if a["title"] and a["title"] != "[Removed]"
    ]