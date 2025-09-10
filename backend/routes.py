from fastapi import APIRouter
from backend.models import Feedback
from backend.sentiments import check_sentiment

router = APIRouter()

@router.get("/")
def read_root():
    return {
        "message": "Welcome to My Sentiment Analysis API 🎉",
        "About": "Live backend service for my Sentiment_Analysis Project backed by Render ",
        "endpoints": {
            "Analyze Sentiment": "/analyze",
            "API Docs": "/docs"
        }
    }
    
@router.post("/analyze")
def analyze_feedback(feedback: Feedback):
    sentiment = check_sentiment(feedback.text)
    return {"feedback": feedback.text, "sentiment": sentiment}
