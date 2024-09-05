# Blog Sentiment Analyzer

This project is a web-based tool that allows you to analyze the sentiment of blog posts using web scraping and natural language processing (NLP). It scrapes or crawls a given blog URL, processes the text, and outputs the sentiment scores (Positive, Neutral, Negative) out of 100. The analysis uses the NLTK library's SentimentIntensityAnalyzer.

## Features

- Scrape or crawl blog posts from a given URL
- Sentiment analysis using NLTK's VADER sentiment analysis
- Displays sentiment scores (Positive, Neutral, Negative) as a percentage
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
    git clone https://github.com/yourusername/blog-sentiment-analyzer.git
    cd blog-sentiment-analyzer
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

1. Enter the URL of the blog post you want to analyze.
2. Choose between "scrape" or "crawl" mode.
3. Click "Analyze Sentiment."
4. View the sentiment analysis results, which will display positive, neutral, and negative scores out of 100, along with the overall sentiment.
5. Optionally, download the sentiment report.

## License

This project is licensed under the MIT License.

## Contributions

Feel free to contribute by submitting issues or pull requests. Any contributions are welcome!
