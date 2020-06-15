import requests
import json
from tkinter import messagebox

class Find_User():
    def __init__(self, id, email):
        self.id=id
        self.email=email

    def find_ID(self, fid=[]):
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
            "email": self.email,
        }

        # Request GET
        try:
            response = requests.get(URL, data=json.dumps(data), headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        response_ID = json.loads(response.text)
        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 200
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

        if 'username' in response_ID:
            fid.append(response_ID['username'])
        else:
            fid.append('None')


    def find_PW(self, fPW=[]):
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
            "username": self.id,
            "email": self.email
        }

        # Request GET
        try:
            response = requests.get(URL, data=json.dumps(data), headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        response_PW = json.loads(response.text)
        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 200
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열
        if 'alert' in response_PW:
            fPW.append(response_PW['alert'])
        else:
            fPW.append('None')
