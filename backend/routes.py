from fastapi import APIRouter
from models import Feedback
from sentiments import check_sentiment

router = APIRouter()

@router.post("/analyze")
def analyze_feedback(feedback: Feedback):
    sentiment = check_sentiment(feedback.text)
    return {"feedback": feedback.text, "sentiment": sentiment}
