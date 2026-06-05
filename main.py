from fetcher import fetch_headlines

topic = input("Enter a topic: ")
articles = fetch_headlines(topic)

for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")
    print(f"   Source: {article['source']} | Date: {article['published']}")
    print("---")