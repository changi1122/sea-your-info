import requests
import json

# user의 token으로 슈퍼 유저인지 확인하는 샘플 코드입니다.

# 실행전 확인 : URL 설정, token

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/issuperuser/"
# URL = "http://localhost:8000/issuperuser/" # 자기 컴퓨터에서 서버를 실행한 경우


# Request POST
response = requests.post(URL, headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
