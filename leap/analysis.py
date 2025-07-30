from textblob import TextBlob
from keybert import KeyBERT

# Sentiment analysis using TextBlob
def analyze_sentiment(texts):
    sentiments = []
    for text in texts:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            sentiments.append('positive')
        elif polarity < -0.1:
            sentiments.append('negative')
        else:
            sentiments.append('neutral')
    return sentiments

# Keyword extraction using KeyBERT
def extract_keywords(texts, top_n=10):
    kw_model = KeyBERT()
    all_keywords = []
    for text in texts:
        keywords = kw_model.extract_keywords(text, top_n=top_n, stop_words='english')
        all_keywords.extend([kw[0] for kw in keywords])
    return all_keywords 