
import os
import streamlit as st
import requests

# Get backend URL from environment variable, default to localhost for local runs
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="Tweet Sentiment Analysis", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    .big-font {
        font-size: 2.2rem !important;
        font-weight: 700;
        color: #1DA1F2;
    }
    .sentiment-box {
        padding: 1.2em;
        border-radius: 0.5em;
        background-color: #f0f2f6;
        margin-top: 1em;
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="big-font">Tweet Sentiment Analysis 💬</div>', unsafe_allow_html=True)
st.write("Analyze the sentiment of any tweet instantly using AI-powered sentiment analysis.")
# Input box for tweet
tweet_text = st.text_area("Enter your tweet:", height=100, max_chars=280, placeholder="What's happening?")



# Button to trigger analysis
if st.button("Analyze Sentiment"):
    if tweet_text:
        try:
           # Send request to backend
            response = requests.post(f"{BACKEND_URL}/analyze", json={"text": tweet_text})
            response.raise_for_status()
            result = response.json()

            sentiment_colors = {
                    "positive": "#d4edda",
                    "negative": "#f8d7da",
                    "neutral": "#fff3cd"
                }
            sentiment = result["sentiment"]
            color = sentiment_colors.get(sentiment, "#f0f2f6")

            st.markdown(
                    f"""
                    <div class="sentiment-box" style="background-color: {color};">
                        <strong>Tweet:</strong> {result['text']}<br>
                        <strong>Sentiment:</strong> <span style="text-transform:capitalize;">{sentiment}</span><br>
                        <strong>Scores:</strong> {result['scores']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            
            # Display results
            #st.write(f"**Tweet**: {result['text']}")
            #st.write(f"**Sentiment**: {result['sentiment'].capitalize()}")
            #st.write(f"**Scores**: {result['scores']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
    else:
        st.warning("Please enter a tweet to analyze.")