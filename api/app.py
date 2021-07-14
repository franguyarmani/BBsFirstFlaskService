import time
import feedparser
from flask import Flask

app = Flask(__name__)

feed_url = "http://feeds.marketwatch.com/marketwatch/marketpulse/.rss"

@app.route('/title')
def get_title():
    title = feedparser.parse(feed_url).feed.title
    return {'title': title}

@app.route('/feed')
def get_feed():
    feed = feedparser.parse(feed_url)
    return {'feed': feed.feed}

@app.route('/links')
def get_links():
    feed = feedparser.parse(feed_url).feed
    return {'links': feed.links}

@app.route('/summaries')
def get_summaries():
    feed = feedparser.parse(feed_url)
    summaries = [x.summary for x in feed.entries]
    return {'summaries': summaries}