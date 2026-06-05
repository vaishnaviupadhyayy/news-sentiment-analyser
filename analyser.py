from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyse_sentiment(articles: list[dict]) -> list[dict]:
    titles = [a["title"] for a in articles]
    results = sentiment_model(titles, truncation=True)
    for article, result in zip(articles, results):
        article["sentiment"] = result["label"]
        article["confidence"] = round(result["score"] * 100, 1)
    return articles