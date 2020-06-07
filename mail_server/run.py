import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mail_server.select_user import *
from mail_server.select_post import *
from datetime import datetime

def sender(recidpients, sw_post, department_post):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('syi.superuser@gmail.com','hxuglvvfbtxjhdqr')
    body=""
    today = datetime.today()

    for item in range(0, len(recidpients)):
        print('이메일 보내는중 :' + recidpients[item])
        msg =MIMEMultipart('alternative')

        msg['Subject']= str(today.month) + '월 ' + str(today.day) + '일 공지사항 데일리 리포트'
        msg['From'] = 'syi.superuser@gmail.com'
        msg['To'] = recidpients[item]

        # 학교 공지사항 body
        department_body = ''
        for i in range(0, len(department_post)):
            department_body += '''\
                <div style="margin: 10px 0">
                    <p style="font-size: 20px; margin: 0; font-weight: bold; margin-bottom: 2px;"><a style="color: black;" href="''' + department_post[i]['url'] + '''"target="_blank">''' + department_post[i]['title'] + '''</a></p>
                    <p style="margin: 0;"><span style="background-color: gray; font-size: 14px; color: white; padding: 1px 4px; border-radius: 3px;">''' + str(department_post[i]['date'])[:str(department_post[i]['date']).index('T')] + '''</span> <span style="margin-left: 16px; background-color: #92234e; font-size: 14px; color: white; padding: 1px 4px; border-radius: 3px;">''' + department_post[i]['type'] + '''</span></p>
                </div>
            '''

        # 학과 공지사항 body
        sw_body = ''
        for i in range(0, len(sw_post)):
            sw_body += '''\
                <div style="margin: 10px 0">
                    <p style="font-size: 20px; margin: 0; font-weight: bold; margin-bottom: 2px;"><a style="color: black;" href="''' + sw_post[i]['url'] + '''"target="_blank">''' + sw_post[i]['title'] + '''</a></p>
                    <p style="margin: 0;"><span style="background-color: gray; font-size: 14px; color: white; padding: 1px 4px; border-radius: 3px;">''' + str(sw_post[i]['date'])[:str(sw_post[i]['date']).index('T')] + '''</span> <span style="margin-left: 16px; background-color: #92234e; font-size: 14px; color: white; padding: 1px 4px; border-radius: 3px;">''' + sw_post[i]['type'] + '''</span></p>
                </div>
            '''
        department_body_with_header = ''
        if department_body != '':
            department_body_with_header = '''
                <div style="margin: 20px 0 20px;">
                    <p style="font-size: 24px; margin: 0; font-weight: bold;">충북대학교 공지사항</p>
                </div>
                <span>''' + department_body + '''</span>
            '''

        sw_body_with_header = ''
        if sw_body != '':
            sw_body_with_header = '''
                <div style="margin: 50px 0 20px;">
                    <p style="font-size: 24px; margin: 0; font-weight: bold;">소프트웨어학과 공지사항</p>
                </div>
                <span>''' + sw_body + '''</span>
            '''

        body = """\
        <html lang="ko">
            <head>
                <meta charset="UTF-8">
                <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR:400,700&amp;display=swap" rel="stylesheet">
            </head>
            <body style="margin: 0; padding: 0; border: 0; font-size: 100%; font: inherit; vertical-align: baseline; line-height: 1.5; font-family: Noto Sans KR, Apple SD Gothic Neo, Malgun Gothic, sans-serif; font-size: 16px;">
                <div style="margin: 10px 20px; padding: 10px 0; font-size: 28px; border-bottom: 1px solid lightgray; text-align: center;">
                    <b>6월 6일 공지사항 데일리 리포트</b>
                </div>
                <div style="margin: 10px 20px 40px;">""" + department_body_with_header + sw_body_with_header + """</div>
                <div style="margin: 40px 20px;">
                    <p style="color: gray; margin: 0;">이 리포트는 <b>정보바다(Sea your info)</b>에서 전송한 공지사항 갈무리입니다. </p>
                    <p style="margin: 0; margin-top: 10px; color: gray"><b>정보바다(Sea your info)</b>에 가입한 적이 없거나, 수신 차단, 탈퇴하고 싶다면 <a href="mailto:syi.superuser@gmail.com">syi.superuser@gmail.com</a>으로 문의하세요.</p>
                </div>
            </body>
        </html>
        """

        msg.attach(MIMEText(body, 'html'))

        server.send_message(msg)

    print('이메일 보내기 완료')
    server.quit()


if __name__ == '__main__':
    list_json = []
    sw_post=[]
    department_post=[]
    School(department_post)
    Software(sw_post)
    selectUser(list_json)

    if len(sw_post) != 0 or len(department_post) != 0:
        sender(list_json, sw_post, department_post)
