from makewordclouds import FeedService
import textutilities.HelperFunctions as h
from wordcloud import WordCloud

def get_texts():
    return FeedService.list_summaries("http://feeds.marketwatch.com/marketwatch/marketpulse/.rss")

def marketwatch_wordcloud():
    cleanText = ' '.join(h.make_wordbank(get_texts()))
    wordCloud = WordCloud().generate(cleanText)
    print("cloud made")
    image = wordCloud.to_image()
    image.show()



