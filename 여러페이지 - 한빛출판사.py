## 한빛출판사 ##
# 1 ~ 5페이지
# 도서제목, 저자, 가격
# import time
import requests
from lxml import html

url = "https://www.hanbit.co.kr/store/books/new_book_list.html"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
# 네이버 -> F12(개발자도구) -> 네트워크 -> 새로고침 -> www.naver.com -> user-agent : 'Mozilla~~ 복사

titles, writers, prices = [], [], []

for i in range(1, 5 + 1):
    params = {'page': i}  # 파라미터(page) 페이지 번호
    res = requests.get(url, headers=headers, params=params)
    htmls = html.fromstring(res.text)       # html -> htmls

    for title in htmls.cssselect('p.book_tit a'):       # html -> htmls
        titles.append(title.text_content())

    for writer in htmls.cssselect('p.book_writer'):     # html -> htmls
        writers.append(writer.text_content())

    for price in htmls.cssselect('span.price'):         # html -> htmls
        price = price.text_content()
        price = price.replace(',', '')
        price = price.replace('원', '')
        prices.append(price)

    # time.sleep(2) # 2초동안 잠시 대기

print(titles[80:])  # 5페이지 도서목록