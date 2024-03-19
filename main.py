import feedparser, time
from urllib.parse import quote

URL = "https://hj-devlog.vercel.app/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 10

markdown_text = """
## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        encoded_link = quote(feed['link'], safe="/:")
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({encoded_link}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
