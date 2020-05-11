## 충북대학교 공식홈페이지 공지사항 크롤러 ##

import requests
import json
from datetime import date
from bs4 import BeautifulSoup   # Javascript 에 조건이 충족되어야만 얻을 수 있는 데이터에 접근하는 것에 한계

html_cbnu = requests.get("https://www.chungbuk.ac.kr/site/www/boardList.do?page=1&boardSeq=112&key=698").text
soup_cbnu = BeautifulSoup(html_cbnu, "html.parser")

# 충북대학교 홈페이지에서 상단의 공지로 올라와있는 게시물은 title과 겹침
select_cbnu = soup_cbnu.select("em")                          # 공지가 붙은 태그의 개수를 세기 위해 parsing
title_cbnu = soup_cbnu.select("td.subject > a ")              # 모든 게시글의 제목 태크 parsing
today = date.today().isoformat()                              # 크롤링을 진행하고 있는 year-month-day 구하기
tempDate_cbnu = soup_cbnu.select("tbody > tr> td")            # 작성일 태크가 들어있는 태그 파싱(가공 전)
uploadDate_cbnu = []                                          # 각 게시물의 작성일 저장(가공 후)
url_cbnu = []                                                 # url 태그 저장할 리스트 선언
todayPost_cbnu = []                                           # 당일 게시된 공지사항의 제목, URL, 작성일을 저장

# tempDate의 정보 중 작성일을 추출하여 uploadDate에 저장(공지까지 포함)
for i in range(5, len(tempDate_cbnu), 6) :
    uploadDate_cbnu.append(tempDate_cbnu[i].text.replace('.', '-'))

# 홈페이지에 공지로 올라온 게시글 및 작성일 배제하는 for 문
for i in range(0, len(select_cbnu)) :
    del title_cbnu[0]
    del uploadDate_cbnu[0]

# 공지사항 url 저장 및 태크 안의 제목을 문자열로 저장
for i in range(0, len(title_cbnu)):
    url_cbnu.append("https://www.chungbuk.ac.kr/site/www" + title_cbnu[i]["href"].lstrip("."))
    title_cbnu[i] = title_cbnu[i].text.strip()
    print(title_cbnu[i] + " " + url_cbnu[i])
print(uploadDate_cbnu)
print()

today = '2020-05-07'   # test case <<48행을 지우고 실행하면 각자 실행시키고 있는 날짜를 기준으로 (주말이라 아무것도 없어서 임의로 지정)

# 당일 올라온 게시글의 제목, url, 작성일을 튜플 형태로 묶어 리스트에 저장
for i in range(0, len(uploadDate_cbnu)):
    if today == uploadDate_cbnu[i] :
        todayPost_cbnu.append((title_cbnu[i], url_cbnu[i], uploadDate_cbnu[i]))
print(todayPost_cbnu)   # 최종 크롤링 결과(제목, URL, 작성일)

print()
print(today + " 크롤링 결과")
for i in range(0, len(todayPost_cbnu)) :
    print(str(i+1) + ". 제목 : " + todayPost_cbnu[i][0] + ", URL : " + todayPost_cbnu[i][1] + ", 작성일 : " + todayPost_cbnu[i][2])
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
for i in range(0, len(todayPost_cbnu)) :
    data = {
        "title": todayPost_cbnu[i][0],
        "date": todayPost_cbnu[i][2]+"T11:11:11.000Z",
        # Date(날짜) 필드는 UTC 시간으로 바꾸고(-9 hour), "YYYY-MM-DDTHH:MM:SS.000Z" 형식으로 전송 필요합니다.
        "url": todayPost_cbnu[i][1],    # 수정 필요
        "type": "scholarship"           # 수정 필요
    }

    # Request POST
    response = requests.post(URL, data=json.dumps(data), headers=headers)

    # 응답 코드, 텍스트 출력
    print("status code : ", response.status_code)  # 성공 : 201
    print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열
