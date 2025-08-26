from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_analyze_positive_tweet():
    sample_tweet = {"text": "I love using Streamlit for apps!"}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    result = response.json()
    assert "sentiment" in result
    assert result["sentiment"] == "positive"
    assert "text" in result
    assert "scores" in result
    assert result["text"] == sample_tweet["text"]

def test_analyze_negative_tweet():
    sample_tweet = {"text": "This app is terrible and buggy."}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    result = response.json()
    assert "sentiment" in result
    assert result["sentiment"] == "negative"
    assert "text" in result
    assert "scores" in result
    assert result["text"] == sample_tweet["text"]

def test_analyze_neutral_tweet():
    sample_tweet = {"text": "The app is okay, nothing special."}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    result = response.json()
    assert "sentiment" in result
    assert result["sentiment"] == "neutral"
    assert "text" in result
    assert "scores" in result
    assert result["text"] == sample_tweet["text"]

def test_analyze_empty_tweet():
    sample_tweet = {"text": ""}
    response = client.post("/analyze", json=sample_tweet)
    assert response.status_code == 200
    result = response.json()
    assert "sentiment" in result
    assert result["sentiment"] == "neutral"
    assert "text" in result
    assert "scores" in result