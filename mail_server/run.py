import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sender(recidpients, sw_post, department_post):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('syi.superuser@gmail.com','hxuglvvfbtxjhdqr')
    body=""

    for item in range(0, len(recidpients)):
        print('이메일 보내는중 :' + recidpients(item))
        msg =MIMEMultipart('alternative')

        msg['Subject']='SeaYourInfo 임시 비밀번호 발급'
        msg['From'] = 'syi.superuser@gmail.com'
        msg['To'] = recidpients(item)

        msg.attach(MIMEText(body, 'html'))

        server.send_message(msg)

    print('이메일 보내기 완료')
    server.quit()


if __name__ == '__main__':
    list_json = []
    sw_post=[]
    department_post=[]
    sender(list_json, sw_post, department_post)