import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

def analyse_sentiment(articles: list[dict]) -> list[dict]:
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    titles = [a["title"] for a in articles]
    response = requests.post(API_URL, headers=headers, json={"inputs": titles})
    results = response.json()
    for article, result in zip(articles, results):
        top = max(result, key=lambda x: x["score"])
        article["sentiment"] = top["label"]
        article["confidence"] = round(top["score"] * 100, 1)
    return articles