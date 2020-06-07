class Make_user():
    def __init__(self, id, emali, pw, subscribe):
        self.id = id
        self.email = emali
        self.pw = pw
        self.subscribe = subscribe

    def make(self, string=[]):
        import requests
        import json
        global response

        # 새로운 user를 생성하는 코드 샘플입니다.
        # 실행전 확인 : URL 설정, data

        # Header : 데이터에 관한 설명
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

        # URL : 목적지 URL
        URL = "http://ras.studio1122.net:8000/user/"
        # URL = "http://localhost:8000/user/"  # 자기 컴퓨터에서 서버를 실행한 경우

        # Data (Dictionary 타입) : 전송할 데이터
        data = {
            "username": self.id,
            "email": self.email,
            "password": self.pw,
            "hasSubscribed": self.subscribe,  # 이메일을 구독했는지 여부 : true면 주기적으로 이메일 전송
            "topics": "none"  # 관심 있는 분야 (리스트를 문자열로 저장), 일단 빈 문자열로 전송
        }

        # Request POST
        response = requests.post(URL, data=json.dumps(data), headers=headers)

        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 201
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

        response_text = json.loads(response.text)
        num = response.status_code
        string.append(num)
        for key in response_text.keys():
            response_text[key] = str(response_text[key]).replace("[\'", "")
            response_text[key] = str(response_text[key]).replace("\']", "")
            string.append(key + " : " + response_text[key])
