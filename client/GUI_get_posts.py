def test(lst=[]):
    import requests
    import json
    # DB의 게시물들을 읽어오는 코드 샘플입니다.
    # 실행전 확인 : URL 설정
    # URL : 목적지 URL

    URL = "http://ras.studio1122.net:8000/posts/"
    # URL = "http://localhost:8000/posts/" 자기 컴퓨터에서 서버를 실행한 경우

    # Request GET
    response = requests.get(URL)

    # 응답 코드, 텍스트 출력
    print("status code : ", response.status_code)  # 성공 : 200
    print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

    # JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
    response_dict = json.loads(response.text)

    for i in range(0, len(response_dict)):
        for key in response_dict[i].keys():
            if key != "type" :
                lst.append(response_dict[i][key])

    return lst