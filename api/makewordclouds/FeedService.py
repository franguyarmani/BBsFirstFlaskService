import feedparser


#feed_url = "http://feeds.marketwatch.com/marketwatch/marketpulse/.rss"

def list_summaries(feed_url):
    feed = feedparser.parse(feed_url)
    return [x.summary for x in feed.entries]