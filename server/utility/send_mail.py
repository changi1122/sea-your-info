import smtplib
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 발신 계정 설정 (Gmail)
# 계정 설정에서 보안 수준이 낮은 앱의 액세스를 허용하여야 합니다!!!
GMAIL_ID = "a@gmail.com"
GMAIL_PASSWORD = "password"


# 임시 비밀번호를 메일로 전송하는 함수
# 매개변수 : destination = 수신자의 메일, new_password = 새로운 비밀번호, username = 로그인 아이디
def send_new_password(destination, new_password, username) :

    sender = GMAIL_ID

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "비밀번호가 변경되었습니다."
    msg['From'] = sender
    msg['To'] = destination

    # Create the body of the message (a plain-text and an HTML version).
    text = "정보바다(Sea your info)의 임시 비밀번호" + new_password
    html = """\
    <html lang="ko">
        <head>
            <meta charset="UTF-8">
        </head>
        <body style="margin: 0; padding: 0; border: 0; font-size: 100%; font: inherit; vertical-align: baseline; line-height: 1.5; font-family: Noto Sans KR, Apple SD Gothic Neo, Malgun Gothic, sans-serif; font-size: 16px;">
            <div style="margin: 10px 20px; padding: 10px 0; font-size: 24px; border-bottom: 1px solid lightgray;">
                비밀번호가 <p style="color: #952953; margin: 0;">변경되었습니다.</p>
            </div>
            <div style="margin: 0 20px 20px;">
                <p style="margin: 0;"><b>정보바다(Sea your info)</b>의 <b style="color: #952953; font-weight: normal;">임시비밀번호 발급 내역</b>을 알려드립니다. 로그인 후 <b style="color: #952953; font-weight: normal;">    반드시 비밀번호를 변경</b>하세요.</p>
            </div>
            <div style="margin: 0 40px; padding: 20px 0; font-size: 18px; border-top: 1px solid black; border-bottom: 1px solid black;">
                <ul style="list-style: none;">
                    <li>
                        <span style="display: inline-block; width: 160px; color: gray;">아이디</span><p style="display: inline-block; margin: 0;">""" + username + """</p>
                    </li>
                    <li>
                        <span style="display: inline-block; width: 160px; color: gray;">임시 비밀번호</span><p style="display: inline-block; margin: 0;"><b>""" + new_password + """</b></p>
                    </li>
                    <li>
                        <span style="display: inline-block; width: 160px; color: gray;">발급 일시</span><p style="display: inline-block; margin: 0;">""" + str(datetime.datetime.now()) + """</p>
                   </li>
                </ul>
            </div>
            <div style="margin: 40px 20px;">
                <p style="color: gray; margin: 0;">비밀번호를 재설정한 적이 없는데 메일을 받았다면 다른 사람이 내 계정 정보를 알아내어 접근했을 수 있습니다. 비밀번호를 다시 설정하세요.</p>
                <p style="margin: 0; margin-top: 10px; color: gray"><b>정보바다(Sea your info)</b>에 가입한 적이 없거나, 수신 차단, 탈퇴하고 싶다면 <a href="mailto:changi112242@gmail.com">changi112242@gmail.com</a>으로 문의하세요.</p>
            </div>
        </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    try:
        # Send the message via gmail SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login(GMAIL_ID, GMAIL_PASSWORD)
        mail.sendmail(sender, destination, msg.as_string())
        mail.quit()
    except:
        return 400
    else:
        return 200

