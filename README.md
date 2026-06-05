# News Sentiment Analyser

## What does this project do?
A web app that fetches live news headlines on any topic using NewsAPI,
runs them through a HuggingFace transformer model (DistilBERT) to classify
sentiment as POSITIVE or NEGATIVE, and displays the results with a bar chart.

## Technologies Used
- Python, Flask (web framework)
- HuggingFace Transformers — DistilBERT model for sentiment classification
- NewsAPI — live news headlines
- Matplotlib + Pandas — data visualisation

## How to run it
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your NewsAPI key: `NEWS_API_KEY=your_key`
6. Run: `python3 app.py`
7. Open `http://127.0.0.1:5000` in your browser

## Live Demo:
https://web-production-4eabc.up.railway.app/

## What I learned
- How to use HuggingFace transformer models for NLP tasks
- Identified domain mismatch: DistilBERT was fine-tuned on movie reviews,
  so it misclassified news headlines like "Chrome's fastest shortcut yet" 
  as NEGATIVE 99% — a real-world ML limitation
- Building REST APIs with Flask
- Keeping secrets safe with .env files
