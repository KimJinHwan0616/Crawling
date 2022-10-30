# 코레일 로그인 후 열차예매
# url : https://www.letskorail.com

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By


# 크롬 설정 #
options = webdriver.ChromeOptions()     # 옵션
services = Service(ChromeDriverManager().install())     # 드라이버 자동 설치
chrome = webdriver.Chrome(service=services, options=options)    # 실행
#######################################################
# 브라우저 창 최대
chrome.maximize_window()
time.sleep(1)

chrome.get('https://www.letskorail.com')
#######################################################
# 브라우저 목록(리스트) 확인
# print(chrome.window_handles)   # 확인용

# 팝업창 닫기
chrome.switch_to.window(chrome.window_handles[1])
chrome.close()
time.sleep(1)

# 브라우저 창 이동
chrome.switch_to.window(chrome.window_handles[0])
time.sleep(1)

# 로그인 클릭
chrome.find_element(
    By.CSS_SELECTOR, 'ul.gnb_list li:nth-child(2) a').click()
time.sleep(2)
#######################################################
# 멤버십번호 
txtMember = chrome.find_element(By.ID, 'txtMember')
txtMember.send_keys('2262941486')   # 멤버십번호 입력
time.sleep(1)

# 비밀번호
txtPwd = chrome.find_element(By.ID, 'txtPwd')
txtPwd.send_keys('rtgh0616^^')
time.sleep(1)

# 로그인 버튼( 2가지 )
# chrome.find_element(By.CSS_SELECTOR, 'li.btn_login a').click()
chrome.find_element(By.XPATH, "//img[@alt='확인']").click()
time.sleep(3)
#######################################################
# 팝업창 닫기
print(chrome.window_handles)

chrome.switch_to.window(chrome.window_handles[1])
chrome.close()
time.sleep(1)

chrome.switch_to.window(chrome.window_handles[1])
chrome.close()
time.sleep(1)

# 브라우저 창 이동
chrome.switch_to.window(chrome.window_handles[0])
time.sleep(1)

# 예매하기 버튼
chrome.find_element(By.XPATH, "//img[@alt='승차권예매']").click()
#######################################################
# 좌석종류 선택
seat01 = Select( chrome.find_element(By.ID, 'seat01') )  # 기본
seat01.select_by_visible_text('창측좌석')
time.sleep(1)

seat02 = Select( chrome.find_element(By.ID, 'seat02') )  # 좌석방향
seat02.select_by_visible_text('순방향석')
time.sleep(1)

# 예매정보
chrome.find_element(By.XPATH, "//input[@title='KTX']").click()
time.sleep(1)

start = chrome.find_element(By.XPATH, "//input[@id='start']")
start.clear()
start.send_keys('서울')

get = chrome.find_element(By.XPATH, "//input[@id='get']")
get.clear()
get.send_keys('부산')

s_year = Select(chrome.find_element(By.ID, 's_year'))
s_year.select_by_visible_text('2022')
time.sleep(1)

s_month = Select(chrome.find_element(By.ID, 's_month'))
s_month.select_by_visible_text('8')
time.sleep(1)

s_day = Select(chrome.find_element(By.ID, 's_day'))
s_day.select_by_visible_text('15')
time.sleep(1)

s_hour = Select(chrome.find_element(By.ID, 's_hour'))
s_hour.select_by_visible_text('2 (오전02)')
time.sleep(1)

# 조회하기 버튼
chrome.find_element(By.XPATH, "//img[@alt='조회하기']").click()
time.sleep(3)
#######################################################
# 아래 스크롤
chrome.execute_script('window.scrollTo(0, 1000);')
time.sleep(1)

# 예매 버튼 ( 계속 변경 )
chrome.find_element(By.XPATH, "//img[@name='btnRsv1_0']").click()
time.sleep(1)
#######################################################
# 경고창 확인
chrome.switch_to.alert.accept()
time.sleep(1)

chrome.switch_to.alert.accept()
time.sleep(1)

# 크롬 드라이버 종료
chrome.close()