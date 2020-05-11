## 충북대학교 소프트웨어학과 공지사항 크롤러 ##
""" 아무래도 소프트웨어학과 홈페이지가 javascript에서 조건은 충족시켜주지 못하는 부분이 존재하는듯
    -> GET javascript:void(0) net::ERR_UNKNOWN_URL_SCHEME 발생
    >> BeautifulSoup + Selenium 사용"""

import requests
import json
import time
from datetime import date
from selenium import webdriver      # 각자 크롬 웹드라이버를 설치해야 함
from bs4 import BeautifulSoup

# 크롬창을 띄우지 않는 옵션 놓기(headless)  << 궁금하신 분들은 밑의 세줄을 지우고 실행 -> sw 홈페이지가 열림
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

driver = webdriver.Chrome("C:\\Users\\yu01g\\PycharmProjects\\chromedriver", options=options)   # 각자 설치하고 압축해제한 chromedriver.exe 파일의 경로 작성 (옵션 삭제X)
driver.get('https://software.cbnu.ac.kr/bbs/bbs.php?db=notice&pgID=ID12415888101')
# time.sleep(1)

html_sw = driver.page_source
soup_sw = BeautifulSoup(html_sw, "html.parser")
title_sw = soup_sw.select("nobr > a")                # 모든 게시글의 제목 태크 parsing
today = date.today().isoformat()                     # 크롤링을 진행하고 있는 year-month-day 구하기
tempDate_sw = soup_sw.select("td.body_num")          # 작성일이 들어있는 태그 저장
uploadDate_sw = []                                   # 게시글의 작성일을 문자열로 저장
url_sw = []                                          # 게시글의 URL 저장
todayPost_sw = []                                    # 당일 게시된 공지사항의 제목, URL, 작성일을 저장

''' 확인 차 삽입(추후 삭제)
for i in range(0, len(tempDate_sw)):
    print(tempDate_sw[i])
'''

# 태그 안에 들어있는 게시글의 제목을 문자열로 저장 및 URL 추출
for i in range(0, len(title_sw)):
    url_sw.append("https://software.cbnu.ac.kr" + title_sw[i]["href"])
    title_sw[i] = title_sw[i].text
    print(title_sw[i] + " " + url_sw[i])
print()

# 태그 안에 들어있는 작성일 추출
for i in range(2, len(tempDate_sw), 4):
    uploadDate_sw.append(tempDate_sw[i].text)
print(uploadDate_sw)
print()

today = '2020-04-27'    # test case <<48행을 지우고 실행하면 각자 실행시키고 있는 날짜를 기준으로 (주말이라 아무것도 없어서 임의로 지정)

# 당일 작성된 게시글의 정보 저장
for i in range(0, len(title_sw)):
    if today == uploadDate_sw[i]:
        todayPost_sw.append((title_sw[i], url_sw[i], uploadDate_sw[i]))
print(todayPost_sw)     # 최종 크롤링 결과(제목, URL, 작성일)

print()
print(today + " 크롤링 결과")
for i in range(0, len(todayPost_sw)) :
    print(str(i+1) + ". 제목 : " + todayPost_sw[i][0] + ", URL : " + todayPost_sw[i][1] + ", 작성일 : " + todayPost_sw[i][2])
print()

print("DB에 새로운 게시물을 생성하는 코드 샘플입니다.")
# 실행전 확인 : URL 설정

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/posts/"

# Data (Dictionary 타입) : 전송할 데이터
for i in range(0, len(todayPost_sw)) :
    data = {
        "title": todayPost_sw[i][0],
        "date": todayPost_sw[i][2],
        # Date(날짜) 필드는 UTC 시간으로 바꾸고(-9 hour), "YYYY-MM-DDTHH:MM:SS.000Z" 형식으로 전송 필요합니다.
        "url": todayPost_sw[i][1],      # 수정 필요
        "type": "scholarship"           # 수정 필요
    }

    # Request POST
    response = requests.post(URL, data=json.dumps(data), headers=headers)

    # 응답 코드, 텍스트 출력
    print("status code : ", response.status_code)  # 성공 : 201
    print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

