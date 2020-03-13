import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def sendmail(sender, password, recivers, msg):
    smtp_server = smtplib.SMTP('smtp.163.com', 25)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recivers, msg)


def get_filemsg(testfile):
    with open(testfile, 'rb') as f:
        filemsg = MIMEText(f.read(), 'base64', 'utf-8')
        filemsg["Content-Type"] = "application/octet-stream"
        filemsg.add_header('Content-Disposition', 'attachment', filename='test.txt')
    return filemsg


def get_imgmsg(imgfile):
    with open(imgfile, 'rb') as f:
        msgImg = MIMEImage(f.read())
        msgImg.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    return msgImg


def get_multimsg(subject, fro, to, imgfile, textfile, context):
    multimessage = MIMEMultipart()
    multimessage['Subject'] = subject
    multimessage['From'] = fro
    multimessage['To'] = to
    multimessage.attach(MIMEText(context, 'plain', 'utf-8'))
    imgmessage = get_imgmsg(imgfile)
    filemsg = get_filemsg(textfile)
    multimessage.attach(imgmessage)
    multimessage.attach(filemsg)
    return multimessage.as_string()


def main():
    sender = 'l17625924672@163.com'
    password = input("输入邮箱密码:")
    receivers = ['271138425@qq.com', 'long.chen@xiaoyuer.com']
    # msg = get_textmsg('TestEmail', sender, ", ".join(receivers))
    msg = get_multimsg('TestEmail', sender, ", ".join(receivers), 'test.jpg', 'test.txt','测试邮件')
    sendmail(sender, password, receivers, msg)


if __name__ == '__main__':
    main()
