# 아파트 단지 사이트에서 주차장 정보 추출
# url : http://www.k-apt.go.kr/
# 팝업창 닫기 -> '단지정보' -> '우리단지 기본정보' 클릭
# 2022년 06월 서울특별시 강남구 삼성동 아이파크삼성동 클릭
# 관리시설정보 -> 주차대수

import time

from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

# 크롬 설정 #
options = webdriver.ChromeOptions()     # 옵션
services = Service(ChromeDriverManager().install())     # 드라이버 자동 설치
chrome = webdriver.Chrome(service=services, options=options)    # 실행
#######################################################
chrome.maximize_window()
time.sleep(1)

chrome.get('http://www.k-apt.go.kr/')

# 팝업창 닫기1
# chrome.find_elements(By.XPATH, "//button[@class='layerP_close']")[0].click()
# time.sleep(1)
#
# chrome.find_elements(By.XPATH, "//button[@class='layerP_close']")[1].click()
# time.sleep(1)

# 팝업창 닫기2   ( 추천 )
chrome.find_element(By.CSS_SELECTOR,
                     "#layerPopup20211208 div button").click()
time.sleep(1)

chrome.find_element(By.CSS_SELECTOR,
                     "#layerPopup202204221 div button").click()
time.sleep(1)

# 팝업창 닫기3   ( 추천 )
# chrome.execute_script('closePopupLayer("#layerPopup20211208")')
# time.sleep(1)
#
# chrome.execute_script('closePopupLayer("#layerPopup202204221")')
# time.sleep(1)

# '단지정보' -> '우리단지 기본정보'
chrome.find_element(By.XPATH, "//a[@title='단지정보']").click()
time.sleep(1)

chrome.find_element(By.XPATH, "//a[@title='우리단지 기본정보']").click()
time.sleep(3)
#######################################################
# 2022년 06월 서울특별시 강남구 삼성동 삼성동센트럴아이파크
year = Select(chrome.find_element(By.NAME, 'searchYYYY'))
year.select_by_visible_text('2022년')
time.sleep(1)

month = Select(chrome.find_element(By.NAME, 'searchMM'))
month.select_by_visible_text('06월')
time.sleep(1)

sido = Select(chrome.find_element(By.NAME, 'combo_SIDO'))
sido.select_by_visible_text('서울특별시')
time.sleep(1)

sgg = Select(chrome.find_element(By.NAME, 'combo_SGG'))
sgg.select_by_visible_text('강남구')
time.sleep(1)

emd = Select(chrome.find_element(By.NAME, 'combo_EMD'))
emd.select_by_visible_text('삼성동')
time.sleep(1)

html = BeautifulSoup(chrome.page_source, 'lxml')
# 아파트 결과 목록 출력
# for apt in html.select('p.aptS_rLName'):
#     print(apt.text)   # 확인용

# 결과 목록 - '아이파크삼성동' 위치 확인
num = 1
for apt in html.select('p.aptS_rLName'):
    if apt.text == '아이파크삼성동': break
    else: num += 1
# print(num)    # 확인용

#mCSB_2_container > ul > li:nth-child(16) > a

# 자동 스크롤
# 결과 목록 각 항목 높이 : 57px
# 현재 화면에 출력된 결과 목록 수 : 4개
# 아이파크삼성동 번호 : 16

# 결과 목록 각 항목 높이
height = elm.size['height']
pos = '-' + str( (num-4) * height ) + 'px'
elm = chrome.find_element(By.CSS_SELECTOR, '#mCSB_2_container')
chrome.execute_script(
    f'arguments[0].style="position: relative; top: {pos}; left: 0px;"', elm)
time.sleep(2)


# 결과 목록 - '아이파크삼성동' 선택  ( 화면에 안 보이면 안 넘어가짐 -> 수정예정 )
chrome.find_element(By.CSS_SELECTOR,
                    f'#mCSB_2_container > ul > li:nth-child({num}) > a').click()
time.sleep(3)
#######################################################
# 관리시설정보 -> 주차대수
chrome.find_element(By.CSS_SELECTOR,
                    'ul.lnbNav li:nth-child(3) a').click()
time.sleep(1)

pcnt = chrome.find_element(By.CSS_SELECTOR, '#kaptd_pcnt').text
pcntu = chrome.find_element(By.CSS_SELECTOR, '#kaptd_pcntu').text
print(pcnt, pcntu)