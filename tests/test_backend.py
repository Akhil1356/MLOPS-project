# tests/test_backend.py

import sys
import os

# Add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from backend.main import app  # Adjust import if your FastAPI app is elsewhere

client = TestClient(app)

def test_analyze_sentiment_positive():
    sample_tweet = {"text": "I love this product!"}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"

def test_analyze_sentiment_negative():
    sample_tweet = {"text": "I hate waiting in line."}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "negative"

def test_analyze_sentiment_neutral():
    sample_tweet = {"text": "It is a Sunday."}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "neutral"

def test_analyze_missing_text_field():
    sample_tweet = {}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 422  # Unprocessable Entity

