from transformers import pipeline
import os

os.environ["TRANSFORMERS_CACHE"] = "/tmp/hf_cache"

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=-1,
    model_kwargs={"low_cpu_mem_usage": True}
)

def analyse_sentiment(articles: list[dict]) -> list[dict]:
    titles = [a["title"] for a in articles]
    results = sentiment_model(titles, truncation=True, max_length=64)
    for article, result in zip(articles, results):
        article["sentiment"] = result["label"]
        article["confidence"] = round(result["score"] * 100, 1)
    return articles