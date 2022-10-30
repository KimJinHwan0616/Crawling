## JTBC ##
# 제목, 미리보기, 카테고리, 기자, 날짜(오전 0~12 & 오후 12~24) 크롤링
# url : https://news.jtbc.co.kr/section/list.aspx?scode=
# 저장 : 리스트 -> json/maria
#######################################################
import requests
from lxml import html
#######################################################
url = 'https://news.jtbc.co.kr/section/list.aspx?scode='
res = requests.get(url)

html = html.fromstring(res.text)
#######################################################
# 데이터 저장 ( 리스트 )
titles, previews, categorys, reporters, dates = [], [], [], [], []

for title in html.cssselect('dt.title_cr a'):
    # print(title.text_content())
    titles.append(title.text_content())

for preview in html.cssselect('dd.read_cr a'):
    # print(preview.text_content())
    preview = preview.text_content().strip()
    # print(preview)
    preview = preview.replace('        ',' ')
    preview = preview.replace('    ',' ')
    preview = preview.replace('   ',' ')
    # print(preview)
    previews.append(preview)

for category in html.cssselect('span.location'):
    # print(category.text_content())
    category = category.text_content().replace('[JTBC', '')
    category = category.replace(']', '')
    category = category.replace('>', '')
    # print(category.strip())
    categorys.append(category.strip())

for reporter in html.cssselect('span.writer'):
    # print(reporter.text_content())
    reporter = reporter.text_content().strip()
    # print(reporter)
    reporters.append(reporter)

for date in html.cssselect('span.date'):
    # print(date.text_content())
    date = date.text_content().strip()
    # print(date)

    spdate = date.split(' ')
    sphour = spdate[2].split(':')

    if spdate[1] == '오후':
        sphour[0] = int(sphour[0]) + 12
    date = f'{spdate[0]} {sphour[0]}:{sphour[1]}:{sphour[2]}'
    # print(date)
    dates.append(date)

# print(len(titles), len(previews), len(reporters), len(categorys), len(dates))    # 확인용
#######################################################
# 데이터 저장 ( 리스트 -> json )
import json
from collections import OrderedDict

jtbc = []
for i in range(len(titles)):
    dic = OrderedDict()

    dic['title'] = titles[i]
    dic['preview'] = previews[i]
    dic['reporter'] = reporters[i]
    dic['category'] = categorys[i]
    dic['date'] = dates[i]

    jtbc.append(dic)

# print(json.dumps( jtbcnews, ensure_ascii=False ) )

with open('./data/JTBC.json', 'a', encoding='UTF-8') as j:
    j.write(json.dumps(jtbc, ensure_ascii=False))
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

sql = 'insert into JTBC values (%s, %s, %s, %s, %s)'    # mariaDB

for i in range(len(titles)):
    params = [ titles[i],previews[i],reporters[i], categorys[i], dates[i] ]

    cur.execute(sql, params)
    conn.commit()

cur.close()
conn.close()
#######################################################
