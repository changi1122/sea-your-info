import requests
import json

# 비밀번호를 찾는 코드 샘플입니다.
# 실행전 확인 : URL 설정, data

# 임시로 응답으로 임시비밀번호를 받게 해두었습니다.
# 실제 작동할 땐 이메일로 전송해야 합니다.

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8',
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/lost-find/find-password/"
# URL = "http://localhost:8000/lost-find/find-password/" # 자기 컴퓨터에서 서버를 실행한 경우

# Data (Dictionary 타입) : 전송할 데이터
data = {
    "username": "normaluser",
    "email": "normaluser@daum.net"
}

# Request GET
response = requests.get(URL, data=json.dumps(data), headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
