## 교보문고 ##
# 도서제목, 저자, 출판사, 출판일, 가격 크롤링
# url : https://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=D0a
# 저장 : 리스트 -> csv/json/maria

import requests
from lxml import html

url = "https://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=D0a"
res = requests.get(url)

html = html.fromstring(res.text)
#######################################################
# 데이터 저장 ( 리스트 )
titles, authors, publishers, dates, prices = [], [], [], [], []

for title in html.cssselect('div.title a strong'):      # 제목
# print(title.text_content())
    titles.append( title.text_content() )
# print(titles)

# for author in html.cssselect('div.author'):
    # print( author.text_content() )

for info in html.cssselect('div.author'):       # 저자, 출판사, 출판일 정보
    info = info.text_content().replace('\r','')
    info = info.replace('\n','')
    info = info.replace('\t','')
    # print(info)

    author = info.split('|')[0]     # 저자
    # print(author)
    authors.append(author)
# print(authors)

    publisher = info.split('|')[1]      # 출판사 
    publisher.strip()       # 공백 왜 안지워지지?

    publishers.append(publisher)
# print(publishers)

    date = info.split('|')[2]       # 출판일
    date.strip()        # 공백 왜 안지워지지?

    dates.append(date)
# print(dates)

for price in html.cssselect('strong.book_price'):     # 가격
    # print(price.text_content())
    price = price.text_content().replace(',','')
    price = price.replace('원','')
    # print(price)
    prices.append(price)
# print(prices)

# print( len(titles), len(authors), len(publishers), len(dates), len(prices) )    # 확인용
#######################################################
# 데이터 저장 ( 리스트 -> csv )
with open('./data/교보문고.csv', 'a', encoding='UTF-8') as c:
    c.write('title;author;publisher;date;price\n')

    for i in range( len( titles )):
        c.write(f'{titles[i]};{authors[i]};{publishers[i].strip()};'
                f'{dates[i].strip()};{prices[i]}\n')
#######################################################
# 데이터 저장 ( csv )
import csv
book = []
for i in range( len( titles ) ):
    dic = [ titles[i], authors[i], publishers[i], dates[i], prices[i] ]
    book.append(dic)
# print(book)

with open('./data/교보문고1.csv', 'w', newline='', encoding='utf8') as c:
    a = csv.writer(c)
    a.writerows(book)

#######################################################
# 데이터 저장 ( 리스트 -> json )
import json
from collections import OrderedDict

kyobo = []
for x in range ( len(titles) ):
    dic = OrderedDict()

    dic['title'] = titles[x]
    dic['author'] = authors[x]
    dic['publisher'] = publishers[x].strip()
    dic['date'] = dates[x].strip()
    dic['price'] = prices[x]

    kyobo.append(dic)

# print(json.dumps( kyobo, ensure_ascii=False ))

with open('./data/교보문고.json', 'a', encoding='UTF-8') as j:
    j.write(json.dumps( kyobo, ensure_ascii=False))
#######################################################
# 데이터 저장 ( maria )
import pymysql

conn = pymysql.connect(
    host='bigdata.c6piwvaa6snp.ap-northeast-2.rds.amazonaws.com',   # 아마존 주소
    database='bigdata',
    user='admin',
    passwd='Bigdata_2022', charset='utf8'
)
cur = conn.cursor()

sql = 'insert into 교보문고 values (%s, %s, %s, %s, %s)'

for i in range( len(titles) ):
    params = [ titles[i], authors[i], publishers[i], dates[i], prices[i] ]

    cur.execute(sql, params)
    conn.commit()

cur.close()
conn.close()