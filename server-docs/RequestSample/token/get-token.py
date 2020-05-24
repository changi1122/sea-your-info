import requests
import json

# user의 token을 읽어오는 샘플 코드입니다. (로그인)
# username과 password를 전송해 token을 받아오면, 해당 토큰을 통해 user임을 확인 받습니다.

# 실행전 확인 : URL 설정, data

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/auth/"
# URL = "http://localhost:8000/auth/" # 자기 컴퓨터에서 서버를 실행한 경우

# Data (Dictionary 타입) : 전송할 데이터
data = {
    "username": "normaluser",
    "password": "password",
}

# Request POST
response = requests.post(URL, data=json.dumps(data), headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열


# JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
response_dict = json.loads(response.text)

# 토큰
print("\n{\"token\" :", response_dict.get("token"))