import requests
import json

# ID를 찾는 코드 샘플입니다.
# 실행전 확인 : URL 설정, data

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8',
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/lost-find/find-id/"
# URL = "http://localhost:8000/lost-find/find-id/" # 자기 컴퓨터에서 서버를 실행한 경우

# Data (Dictionary 타입) : 전송할 데이터
data = {
    "email": "normaluser@daum.net",
}

# Request GET
response = requests.get(URL, data=json.dumps(data), headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
