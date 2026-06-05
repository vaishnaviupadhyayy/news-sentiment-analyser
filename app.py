from flask import Flask, render_template, request
from fetcher import fetch_headlines
from analyser import analyse_sentiment
from visualiser import plot_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    articles = []
    topic = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        articles = fetch_headlines(topic)
        analyse_sentiment(articles)
        plot_sentiment(articles, topic)
    return render_template("index.html", articles=articles, topic=topic)

if __name__ == "__main__":
    app.run(debug=True)