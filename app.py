import streamlit as st
import openai
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

load_dotenv()

firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')
firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)

openai.api_key = os.getenv('OPENAI_API_KEY')

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

st.title("Blog Sentiment Analyzer")
url = st.text_input("Enter the URL of the blog post:")
action = st.selectbox("Choose Action", ["scrape", "crawl"])

if st.button("Analyze Sentiment"):
    if not url:
        st.error("Please enter a URL.")
    else:
        try:
            if action == "scrape":
                scrape_result = firecrawl_app.scrape_url(url, params={'formats': ['markdown']})
                content = scrape_result.get('markdown', '')
            else:
                crawl_status = firecrawl_app.crawl_url(
                    url, 
                    params={'limit': 100, 'scrapeOptions': {'formats': ['markdown']}}
                )
                content = crawl_status.get('markdown', '')

            if content:
                sentiment = sia.polarity_scores(content)
                pos_score = sentiment['pos'] * 100
                neu_score = sentiment['neu'] * 100
                neg_score = sentiment['neg'] * 100

                st.subheader("Sentiment Analysis")
                st.write(f"Positive: {pos_score:.2f}")
                st.write(f"Neutral: {neu_score:.2f}")
                st.write(f"Negative: {neg_score:.2f}")
                st.write(f"Overall Sentiment: {'Positive' if sentiment['compound'] > 0 else 'Negative'}")

                st.download_button("Download Sentiment Report", content, file_name="sentiment_report.txt")

            else:
                st.error("No content found in the scrape/crawl result.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
