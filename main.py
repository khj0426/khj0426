import feedparser, time
from urllib.parse import quote

URL = "https://hj-devlog.vercel.app/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 10

markdown_text = """

안녕하세요! 프론트엔드 개발자 김효중입니다.

- 늘 편안한 팀원이 되고자 하는 프론트엔드 개발자 김효중입니다. 
- 기술을 선택할 때 “왜”라는 물음을 집요하게 파고들며 함께 성장하는 즐거움과,깊이 학습하는 것의 중요성을 알고 있습니다.

## ✅ 최근 블로그 글

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
