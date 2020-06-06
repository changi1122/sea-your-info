import requests
import json

# user 전체 정보를 읽어오는 코드 샘플입니다.
# 실행전 확인 : URL 설정, token 설정

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # 관리자 토큰
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/user/"
# URL = "http://localhost:8000/user/test/" # 자기 컴퓨터에서 서버를 실행한 경우


# Request GET
response = requests.get(URL, headers=headers)



# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열

# JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
response_dict = json.loads(response.text)
print("json to dict : ", response_dict)


# Dictionary 타입 배열 출력
print("\nDictionary 타입 배열 : ")
print("[")

for i in range(0, len(response_dict)):
    print("\t{")
    for key in response_dict[i].keys():
        print("\t\t", key, " : ", response_dict[i][key])
    print("\t},")

print("]")
