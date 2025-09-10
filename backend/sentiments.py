import nltk
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer
# Initialize analyzer once (good for performance)
sia = SentimentIntensityAnalyzer()

def check_sentiment(feedback: str) -> str:
    """Analyze the sentiment of a given feedback string."""
    score = sia.polarity_scores(feedback)
    compound = score['compound']

    if compound >= 0.05:
        return "Positive 😊"
    elif compound <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"
    