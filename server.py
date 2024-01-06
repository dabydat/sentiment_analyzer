"""Module providing a function printing python version."""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Comments about sent_analyzer"""
    text_to_analyze = request.args.get("textToAnalyze")
    text_analized = sentiment_analyzer(text_to_analyze)
    label = text_analized['label']
    score = text_analized['score']
    if label is None:
        return "There is an error trying to analize that text, try again with another one."
    return f"The text has been identified as {label} with a score of {score}"

@app.route("/")
def render_index_page():
    """Comments about render_index_page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
