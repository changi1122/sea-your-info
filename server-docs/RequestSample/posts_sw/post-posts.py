import requests
import json

# DB에 새로운 게시물을 생성하는 코드 샘플입니다.
# 실행전 확인 : URL 설정

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/posts_sw/"
# URL = "http://localhost:8000/posts_sw/" # 자기 컴퓨터에서 서버를 실행한 경우

# Data (Dictionary 타입) : 전송할 데이터
data = {
    "title": "[안내] 한국장학재단 저금리 전환대출 시행 안내",
    "date": "2020-05-07T03:44:19.000Z",
    # Date(날짜) 필드는 UTC 시간으로 바꾸고(-9 hour), "YYYY-MM-DDTHH:MM:SS.000Z" 형식으로 전송 필요합니다.
    "url": "https://software.cbnu.ac.kr/bbs/bbs.php?task=view&db=notice&no=7202&category=0",
    "type": "scholarship"
}

# Request POST
response = requests.post(URL, data=json.dumps(data), headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
