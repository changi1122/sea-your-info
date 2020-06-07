import requests
import json


class Update_User():
    def __init__(self, id, email, pw, new_pw, Token, subscribe):
        self.username = id
        self.email = email
        self.pw = pw
        self.new_pw = new_pw
        self.token = Token
        self.subscribe = subscribe

    def UUD_INFO(self, string=[]):
        # user 정보를 수정하는 코드 샘플입니다.
        # 실행전 확인 : URL 설정, username 설정, token 설정, data

        # Header : 데이터에 관한 설명
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Token ' + self.token  # 해당 유저 토큰 or 관리자 토큰
        }

        # URL : 목적지 URL
        URL = "http://ras.studio1122.net:8000/user/"
        # URL = "http://localhost:8000/user/" # 자기 컴퓨터에서 서버를 실행한 경우

        # Username
        username = self.username

        integratedURL = URL + username + "/"

        # Data (Dictionary 타입) : 전송할 데이터
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.pw,  # 현재 비밀번호 : 필수
            "new_password": self.new_pw,  # 새로운 비밀번호 : 이 줄을 삭제하면 비밀번호 유지
            "hasSubscribed": self.subscribe,  # 이메일을 구독했는지 여부 : true면 주기적으로 이메일 전송
            "topics": "none"  # 관심 있는 분야 (리스트를 문자열로 저장)
        }

        # Request PUT
        response = requests.put(integratedURL, data=json.dumps(data), headers=headers)

        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 201
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열
        num = response.status_code
        string.append(num)
