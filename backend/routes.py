from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from backend.models import Feedback
from backend.sentiments import check_sentiment

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def read_root():
    frontend_url = "https://sentiment-analysis-five-beta.vercel.app/"
    return f"""
    <html>
        <head>
            <title>Sentiment Analysis API</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 40px;
                    color: #333;
                }}
                h1 {{
                    color: #8e3535;
                }}
                a {{
                    color: #0066cc;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .endpoint {{
                    margin-left: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>Welcome to My Sentiment Analysis API 🎉</h1>
            <p><strong>About:</strong> Live backend service for my Sentiment_Analysis Project backed by Render</p>
            <p><strong>Frontend:</strong> <a href="{frontend_url}" target="_blank">{frontend_url}</a></p>
            <h2>Endpoints:</h2>
            <p class="endpoint"><strong>Analyze Sentiment:</strong> <a href="/analyze">/analyze</a></p>
            <p class="endpoint"><strong>API Docs:</strong> <a href="/docs">/docs</a></p>
        </body>
    </html>
    """
  
@router.post("/analyze")
def analyze_feedback(feedback: Feedback):
    sentiment = check_sentiment(feedback.text)
    return {"feedback": feedback.text, "sentiment": sentiment}
