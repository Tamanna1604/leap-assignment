import snscrape.modules.twitter as sntwitter
import praw
import requests

# Twitter scraping using snscrape
def fetch_twitter_mentions(query, limit=50):
    results = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'"{query}"').get_items()):
        if i >= limit:
            break
        results.append({
            'text': tweet.content,
            'url': f'https://twitter.com/{tweet.user.username}/status/{tweet.id}'
        })
    return results

# Reddit scraping using praw (requires Reddit API credentials)
def fetch_reddit_mentions(query, limit=50):
    # TODO: Replace with your Reddit API credentials
    reddit = praw.Reddit(client_id='SUedSg4rUB_ofid4fs8HRg',
                         client_secret='EtTr2Rjw2YhXF-qQ0KmHHERLNFXvYQ',
                         user_agent='leap_mvp/0.1')
    results = []
    for submission in reddit.subreddit('all').search(query, limit=limit):
        results.append({
            'text': submission.title + '\n' + submission.selftext,
            'url': submission.url
        })
    return results

# News scraping using NewsAPI (requires API key)
def fetch_news_mentions(query, api_key='76fe58a277aa451fa204d1ba8150508b', limit=50):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&pageSize={limit}'
    try:
        resp = requests.get(url)
        data = resp.json()
        articles = data.get('articles', [])
        return [{
            'text': a['title'] + '\n' + a.get('description', ''),
            'url': a['url']
        } for a in articles]
    except Exception as e:
        return [] 