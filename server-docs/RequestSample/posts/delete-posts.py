import requests
import json

# DB의 게시물을 삭제하는 코드 샘플입니다. 삭제할 게시물의 id가 필요합니다.
# 실행전 확인 : URL 설정, ID 값 설정

# Header : 데이터에 관한 설명
headers = {
    'Authorization': 'Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# URL
URL = "http://ras.studio1122.net:8000/posts/"
# URL = "http://localhost:8000/posts/" # 자기 컴퓨터에서 서버를 실행한 경우

# ID
ID = "2"                        # 변수!!! 실행전 설정 필수!!!

integratedURL = URL + ID + "/"

# Request DELETE : id가 ID인 게시물을 삭제합니다.
response = requests.delete(integratedURL, headers=headers)

# 응답 코드, 텍스트 출력
print(response.text)
