import feedparser, time
from urllib.parse import quote

URL = "https://hj-devlog.vercel.app/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 10

markdown_text = """

안녕하세요! 프론트엔드 개발자 김효중입니다.

늘 편안한 팀원이 되고자 하는 프론트엔드 개발자 김효중입니다. 기술을 선택할 때 “왜”라는 물음을 집요하게 파고들며 함께 성장하는 즐거움과,깊이 학습하는 것의 중요성을 알고 있습니다.

- 💙 토스증권 프론트엔드 어시스턴트 Product Stability Team (2025.03.10 ~ )
- 💙 주식회사 업사이트 프론트엔드 인턴 (2024.08 ~ 2024.11)
- 💙 프로그래머스 프론트엔드 데브코스 (2023.06 ~ 2023.11)

## 기술적으로 여러 고민 + 해결했던 기록들 모음

- [브라우저의 탭간 데이터 동기화를 BroadCastChannel로 해결했던 경험](https://beaded-menu-418.notion.site/26ec0ea540f780ef800bcb3e57cd3982?pvs=73)
- [usePreservedCallback훅에 대해서](https://beaded-menu-418.notion.site/usePreserverCallback-1fe0e7b922b44910b816b47f78d881a0?pvs=74)
- [tanstack-query와 react-hook-form의 데이터 동기화에 대해서](https://beaded-menu-418.notion.site/invalidateQueries-1c6c0ea540f780d9bcbff3161c6e2926?pvs=74)
- [Next의 하이드레이션 문제를 깔끔하게 해결하는 방법에 대해](https://beaded-menu-418.notion.site/11ea428552764b4a95fc179b3d35c2f4)


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
