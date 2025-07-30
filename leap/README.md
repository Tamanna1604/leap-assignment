# LeapScholar Brand Monitoring MVP

## Problem Statement
The Head of Marketing at LeapScholar needs a quick, automated way to:
- Track public mentions of "LeapScholar" across social media and news
- Understand general sentiment (positive/negative/neutral)
- Spot important conversations and emerging trends
- Get all insights in a simple, actionable format (dashboard/report)

---

## MVP Solution Overview

### Core Features
1. **Collect Mentions**: Scrape mentions of "LeapScholar" from Twitter (X), Reddit, and News sites.
2. **Sentiment Analysis**: Automatically classify mentions as positive, negative, or neutral.
3. **Summarize & Highlight**:
   - Show top mentions (most engagement or relevance)
   - Extract key themes and trending keywords
   - Visualize sentiment and trends
4. **Present Insights**: Display everything in a clean, easy-to-read dashboard.

---

## Technology Choices (Fast, Free, MVP-Ready)

| Feature                | Tool/Library                        |
|------------------------|-------------------------------------|
| Data scraping (Twitter)| `snscrape` (Python, no API key)     |
| Data scraping (Reddit) | `Pushshift` API or `praw`           |
| Data scraping (News)   | `NewsAPI` (free tier) or `requests` |
| Sentiment Analysis     | `TextBlob` (simple)                 |
| Keyword Extraction     | `KeyBERT` or `collections.Counter`  |
| Dashboard              | `Streamlit` (Python, fast UI)       |
| Optional Alerts        | `smtplib` (email), Zapier, IFTTT    |

---

## Implementation Steps

1. **Scrape Data**
   - Use `snscrape` to fetch recent tweets mentioning "LeapScholar"
   - Use Reddit API to fetch posts/comments mentioning "LeapScholar"
   - Use NewsAPI or web scraping for news articles
2. **Analyze Sentiment**
   - Use `TextBlob` to classify each mention
3. **Extract Trends & Highlights**
   - Use `KeyBERT` or `Counter` to find top keywords/themes
   - Select top mentions by engagement or recency
4. **Build Dashboard**
   - Use `Streamlit` to display:
     - Sentiment breakdown (pie/bar chart)
     - Top mentions (with links)
     - Trending keywords/themes
     - Time series of mentions
5. **(Optional) Email Alerts**
   - Use `smtplib` or Zapier to send daily/weekly highlights

---

## Loom Video Script Outline

1. **Intro (10s)**
   - "Hi, this is a quick demo of my MVP for LeapScholar brand monitoring."
2. **Show Dashboard (30s)**
   - Walk through the Streamlit dashboard: sentiment chart, top mentions, trends
3. **Explain Approach (40s)**
   - "I used Python for fast prototyping, with snscrape for Twitter, Pushshift for Reddit, and NewsAPI for news. TextBlob handles sentiment, and KeyBERT/Counter extracts trends. Streamlit makes the dashboard simple and interactive."
   - "This format gives the Marketing Head a daily snapshot—no manual searching, just actionable insights."
4. **Wrap Up (10s)**
   - "Thanks for watching! Happy to answer questions."

---

## Why This Format?
- **Fast**: All tools are free, easy to set up, and require minimal coding.
- **Actionable**: Dashboard summarizes everything at a glance—perfect for a busy executive.
- **Scalable**: Can add more platforms or deeper analysis later.

---

## Tools Used
- Python (snscrape, praw, requests, TextBlob, KeyBERT, Streamlit)
- (Optional) Zapier/IFTTT for alerts

---

## Next Steps (if more time)
- Add more platforms (Instagram, Facebook)
- Use advanced NLP (HuggingFace Transformers)
- Deploy dashboard online (Streamlit Cloud) 