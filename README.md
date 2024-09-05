# Sentix

Sentix is a web-based tool for analyzing the sentiment of blog posts using web scraping and natural language processing (NLP). It scrapes or crawls a given blog URL, processes the text, and provides sentiment scores (Positive, Neutral, Negative) out of 100. The analysis uses NLTK's VADER sentiment analysis.

## Features

- Scrape or crawl blog posts from a given URL
- Sentiment analysis using NLTK's VADER sentiment analyzer
- Displays sentiment scores (Positive, Neutral, Negative) as percentages
- Overall sentiment classification (Positive or Negative)
- Downloadable sentiment report

## Technologies Used

- [Streamlit](https://streamlit.io/) for the web interface
- [OpenAI](https://openai.com/) for content processing (optional)
- [Firecrawl](https://github.com/mendable-ai/firecrawl) for scraping and crawling blog content
- [NLTK](https://www.nltk.org/) for sentiment analysis
- Python for backend logic

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/harshsbhat/sentix.git
    cd sentix
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file to store your API keys:

    ```bash
    touch .env
    ```

    Add the following lines to the `.env` file:

    ```env
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

## Video

https://www.loom.com/share/237cc669abf44d73bc406709fc0bc5fa?sid=5828fe9e-836b-4043-a505-0627b739701f

1. Enter the URL of the blog post you want to analyze.
2. Choose between "scrape" or "crawl" mode.
3. Click "Analyze Sentiment."
4. View the sentiment analysis results, which will display positive, neutral, and negative scores out of 100, along with the overall sentiment.
5. Optionally, download the sentiment report.
