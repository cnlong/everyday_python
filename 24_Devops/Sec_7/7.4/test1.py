import  smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.163.com"
SMTP_PORT = 25

def send_main(user, pwd, to, subject, text):
    # 创建一个纯文本对象
    msg = MIMEText(text)
    # 添加收件人，发件人，邮件主题
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    print('Connecting to Mail Server.')
    try:
        smtp_server.ehlo()
        print("Starting Encrypted Section")
        smtp_server.starttls()
        smtp_server.ehlo()
        print("Logging Into Mail Server")
        smtp_server.login(user, pwd)
        print("Sending Mail.")
        smtp_server.sendmail(user, to, msg.as_string())
        print("Sending Mail Successful")
    except Exception as err:
        print('Sending Mail Failed:{0}'.format(err))
    finally:
        smtp_server.quit()


def main():
    send_main('l17625924672@163.com', 'chenchen6666', '271138425@qq.com', 'Important', 'Test Message')


if __name__ == '__main__':
    main()