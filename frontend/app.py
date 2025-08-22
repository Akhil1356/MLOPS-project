import streamlit as st
import requests

st.title("Tweet Sentiment Analysis")

# Input box for tweet
tweet_text = st.text_area("Enter your tweet:", height=100)

# Button to trigger analysis
if st.button("Analyze"):
    if tweet_text:
        try:
            # Send request to backend (use localhost for local testing)
            response = requests.post("http://localhost:8000/analyze", json={"text": tweet_text})
            response.raise_for_status()  # Raise exception for bad status codes
            result = response.json()
            
            # Display results
            st.write(f"**Tweet**: {result['text']}")
            st.write(f"**Sentiment**: {result['sentiment'].capitalize()}")
            st.write(f"**Scores**: {result['scores']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
    else:
        st.warning("Please enter a tweet to analyze.")