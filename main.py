import nltk
from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
 
def analyze_sentiment_vader(text):
    sia = SentimentIntensityAnalyzer()
    compound_score = sia.polarity_scores(text)['compound']
    if compound_score >= 0.05:
        return 'Positive'
    elif -0.05 < compound_score < 0.05:
        return 'Neutral'
    else:
        return 'Negative'

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/analyze", methods=['POST'])
def analyze():
    text = request.form['statement']
    result = analyze_sentiment_vader(text)
    return render_template('home.html', result=result, text=text)