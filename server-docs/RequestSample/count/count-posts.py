import requests
import json

# DB의 게시물의 카운터를 1 증가시키는 샘플 코드입니다.
# 실행전 확인 : URL 설정, ID 설정

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/posts_count/"
# URL = "http://localhost:8000/posts_count/" # 자기 컴퓨터에서 서버를 실행한 경우

# 게시물 아이디
ID = "3"

integratedURL = URL + ID + "/"

# Request GET
response = requests.get(URL)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 200
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
