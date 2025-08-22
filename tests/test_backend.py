# tests/test_backend.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_tweet():
    # Sample tweet
    sample_tweet = {"text": "I love using Streamlit for apps!"}
    
    # Send POST request to /analyze
    response = client.post("/analyze", json=sample_tweet)
    
    # Check status code
    assert response.status_code == 200
    
    # Get JSON response
    result = response.json()
    
    # Example assertion: check that sentiment key exists
    assert "sentiment" in result
    
    # Optional: if you have a deterministic sentiment model
    # assert result["sentiment"] == "positive"
