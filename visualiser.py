import matplotlib.pyplot as plt
import pandas as pd

def plot_sentiment(articles: list[dict], topic: str):
    df = pd.DataFrame(articles)
    counts = df["sentiment"].value_counts()
    
    colors = {
        "POSITIVE": "#2ecc71",
        "NEGATIVE": "#e74c3c",
        "NEUTRAL": "#95a5a6"
    }
    
    bar_colors = [colors.get(label, "gray") for label in counts.index]
    
    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar", color=bar_colors)
    plt.title(f"Sentiment Analysis: '{topic}'")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("sentiment_chart.png")
    print("\nChart saved as sentiment_chart.png")