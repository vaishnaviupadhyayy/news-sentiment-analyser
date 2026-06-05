from fetcher import fetch_headlines
from analyser import analyse_sentiment
from visualiser import plot_sentiment
topic = input("Enter a topic: ")
articles = fetch_headlines(topic)
analyse_sentiment(articles)
for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")
    print(f"   Source: {article['source']} | Date: {article['published']} | {article['sentiment']} {article['confidence']}%")
    print("---")
plot_sentiment(articles, topic)