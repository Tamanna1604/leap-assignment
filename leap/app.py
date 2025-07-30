import streamlit as st
from collections import Counter
from scraper import fetch_reddit_mentions, fetch_news_mentions
from analysis import analyze_sentiment, extract_keywords

st.title("LeapScholar Brand Monitoring Dashboard (MVP)")

st.sidebar.header("Settings")
query = st.sidebar.text_input("Brand Keyword", value="LeapScholar")

if st.sidebar.button("Run Analysis"):
    st.info("Fetching mentions and analyzing... (this may take a minute)")
    # Fetch data
    reddit = fetch_reddit_mentions(query)
    news = fetch_news_mentions(query)
    all_mentions = reddit + news
    texts = [m["text"] if isinstance(m, dict) and "text" in m else str(m) for m in all_mentions]

    # Sentiment analysis
    sentiments = analyze_sentiment(texts)
    sentiment_counts = Counter(sentiments)

    # Keyword extraction
    keywords = extract_keywords(texts)
    top_keywords = Counter(keywords).most_common(10)

    # Dashboard sections
    st.subheader("Sentiment Breakdown")
    st.bar_chart(sentiment_counts)

    st.subheader("Top Mentions")
    for mention in all_mentions[:5]:
        if isinstance(mention, dict) and "url" in mention:
            st.markdown(f"[{mention['text'][:100]}...]({mention['url']})")
        else:
            st.write(mention)

    st.subheader("Trending Keywords")
    st.write([kw for kw, _ in top_keywords])

    st.subheader("Mentions Over Time")
    st.write("(Time series chart placeholder)")
else:
    st.write("Enter a brand keyword and click 'Run Analysis' to begin.") 