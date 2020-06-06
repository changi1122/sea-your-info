import requests
import json

# DB에 게시물을 수정하는 코드 샘플입니다.
# 실행전 확인 : URL 설정, ID 값 설정

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Token 76042b6aa0deb34d25aa58eafb82a0425f07f433'
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/posts_sw/"
# URL = "http://localhost:8000/posts/" # 자기 컴퓨터에서 서버를 실행한 경우

# ID : 수정할 게시물의 id
ID = "19"                        # 변수!!! 실행전 설정 필수!!!

integratedURL = URL + ID + "/"

# Data (Dictionary 타입) : 수정할 데이터
data = {
    "title": "[모집]충북인재양성재단 2020학년도 상반기 장학생 선발 안내(~3/20)",
    "date": "2020-05-07T03:44:19.000Z",
    # Date(날짜) 필드는 UTC 시간으로 바꾸고(-9 hour), "YYYY-MM-DDTHH:MM:SS.000Z" 형식으로 전송 필요합니다.
    "url": "https://software.cbnu.ac.kr/bbs/bbs.php?task=view&db=notice&no=7202&category=0",
    "type": "scholarship",
    "isSent": "True"
}

# Request PUT
response = requests.put(integratedURL, data=json.dumps(data), headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
