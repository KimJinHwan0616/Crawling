# 아파트 단지 사이트에서 주차장 정보 추출
# url : http://www.k-apt.go.kr/
# 팝업창 닫기 -> '단지정보' -> '우리단지 기본정보' 클릭
# 2022년 06월 서울특별시 강남구 삼성동 삼성래미안2차 클릭

import requests

# 우리 단지 검색
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
# 네이버 -> F12(개발자도구) -> 네트워크 -> 새로고침 -> www.naver.com -> user-agent : 'Mozilla~~ 복사

# F12(개발자 도구) -> 네트워크 -> Fetch/XHR -> 새로고침
url1 = 'http://www.k-apt.go.kr/cmmn/bjd/getBjdList.do'  # getBjdList.do
url2 = 'http://www.k-apt.go.kr/kaptinfo/getKaptList.do' # getKaptList.do

# 우리 단지 검색시 시도별 코드 조회
params = {'bjd_code': '', 'bjd_gbn': 'SIDO'}    # getBjdList.do -> 페이로드 -> SIDO
res = requests.get(url1, headers=headers, params=params)
print(res.text)

# 우리 단지 검색시 시군구별 코드 조회
params = {'bjd_code': '11', 'bjd_gbn': 'SGG'}    # getBjdList.do -> 페이로드 -> 11, SGG
res = requests.get(url1, headers=headers, params=params)
print(res.text)

# 우리 단지 검색시 읍면동별 코드 조회
params = {'bjd_code': '11680', 'bjd_gbn': 'EMD'}    # getBjdList.do -> 페이로드 -> 11680, EMD
res = requests.get(url1, headers=headers, params=params)
print(res.text)


# 우리 단지 검색시 시도/시군구/동별 아파트 정보 조회
params = {'bjd_code': '11680105', 'search_date': '202206'}    # getKaptList.do -> 페이로드 -> 11680105, 202206
res = requests.get(url2, headers=headers, params=params)
print(res.text)

# 우리단지 기본정보

# 지정한 아파트 정보 조회
url3 = 'http://www.k-apt.go.kr/cmmn/selectKapt.do'

params = {'bjd_code': '1168010500', 'kapt_code': 'A13509009',
          'search_date': '202206', 'kapt_usedate': '',
          'kapt_name': '', 'go_url': '/kaptinfo/openkaptinfo.do'}    # selectKapt.do -> 페이로드 -> 11680105, 202206
res = requests.get(url3, headers=headers, params=params)
print(res.text)

# 지정한 아파트의 주차장 정보 조회1
params = {'bjd_code': '1168010500', 'kapt_code': 'A13509009',
          'search_date': '202206', 'kapt_usedate': '',
          'kapt_name': '', 'go_url': '/kaptinfo/openKaptMng.do'}    # openKaptMng.do -> 페이로드
res = requests.get(url3, headers=headers, params=params)
print(res.text)     # 관리시설정보 페이지에 대한 html 코드만 출력

# 지정한 아파트의 주차장 정보 조회2
url4 = 'http://www.k-apt.go.kr/kaptinfo/getKaptInfo_detail.do'

params = {'kapt_code': 'A13509009'}    # /getKaptInfo_detail.do -> 페이로드
res = requests.get(url4, headers=headers, params=params)
print(res.text)     # 관리시설정보 페이지에 대한 html 코드만 출력