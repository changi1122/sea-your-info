# 충북대 공지사항
def Get_Department(lst_Dep=[]):
    import requests
    import json
    # DB의 게시물들을 읽어오는 코드 샘플입니다.
    # 실행전 확인 : URL 설정
    # URL : 목적지 URL

    URL = "http://ras.studio1122.net:8000/posts/"
    # URL = "http://localhost:8000/posts/" 자기 컴퓨터에서 서버를 실행한 경우

    # Request GET
    response_Dep = requests.get(URL)

    # 응답 코드, 텍스트 출력
    print("status code : ", response_Dep.status_code)  # 성공 : 200
    print("response text : ", response_Dep.text)  # 응답 텍스트 : JSON 형식 문자열

    # JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
    response_dict = json.loads(response_Dep.text)

    for i in range(0, len(response_dict)):
        for key in response_dict[i].keys():
            if key != "type" :
                lst_Dep.append(response_dict[i][key])

    return lst_Dep


# sw학과 공지사항
def Get_SW(lst_sw=[]):
    import requests
    import json
    # DB의 게시물들을 읽어오는 코드 샘플입니다.
    # 실행전 확인 : URL 설정
    # URL : 목적지 URL

    URL = "http://ras.studio1122.net:8000/posts_sw/"
    # URL = "http://localhost:8000/posts/" 자기 컴퓨터에서 서버를 실행한 경우

    # Request GET
    response_sw= requests.get(URL)

    # 응답 코드, 텍스트 출력
    print("status code : ", response_sw.status_code)  # 성공 : 200
    print("response text : ", response_sw.text)  # 응답 텍스트 : JSON 형식 문자열

    # JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
    response_dict_sw = json.loads(response_sw.text)

    for i in range(0, len(response_dict_sw)):
        for key in response_dict_sw[i].keys():
            if key != "type" :
                lst_sw.append(response_dict_sw[i][key])

    return lst_sw