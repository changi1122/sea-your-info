# 유현진
import pymysql

def selectUser():
    i, j = 0, 0
    hasSubscribe = []   # 구독한 사람들의 구독 여부와 id 저장
    subscribeUser = []  # 구독한 사람들의 이메일 저장

    # hasSubscribe의 값을 가져와 구독한 사람의 user_id를 저장
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='yugun1596!@', db='seayourinfo',
                         charset='utf8')
    cursor = db.cursor()
    cursor.execute("SELECT hasSubscribed, user_id FROM user_customuser")

    # seayuorinfo 테이블 중 user_customuser의 내용 출력 (test)
    while (True):
        # 구독 여부가 포함된 테이플의 recode 저장
        recode_S = cursor.fetchone()

        # fetch할 데이터가 없으면
        if recode_S is None:
            break

        # fetch한 데이터 중 hasSubscribe == 0일 경우
        if recode_S[0] == 0:
            continue

        # Subscribe한 사람의 hasSubscribe, user_id 저장
        tuple = (recode_S[0], recode_S[1])
        hasSubscribe.append(tuple)

        # 중요한 것은 모든 SQL명령어는 %s를 사용해서 데이터를 지정해준다
        print("HasSubscribe : %s, User_id : %s" % (hasSubscribe[i][0], hasSubscribe[i][1]))  # test
        i += 1

    # 구독한 사람들의 user_id, email 불러오기
    cursor.execute("SELECT id, email FROM auth_user")

    # 메일 수신을 구독한 사람들의 email 저장
    while (True):
        # 가입한 사람들의 email이 포함된 recode 저장
        recode_E = cursor.fetchone()

        # fetch할 데이터가 없으면
        if recode_E is None:
            break
        # fetch한 recode의 id와 구독 list에 저장된 id와 같지 않을 경우
        if recode_E[0] != hasSubscribe[j][1]:
            continue  # 테이블의 다음 recode로 넘어감

        # 메일 수신을 구독한 사람들의 email 저장
        subscribeUser.append(recode_E[1])
        print("Email : %s" % (subscribeUser[j]))  # test
        j += 1

    db.close()