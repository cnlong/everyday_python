import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender = 'l17625924672@163.com'
password = 'chenchen6666'
receivers = ['271138425@qq.com', 'long.chen@xiaoyuer.com']

COMMASPACE = ", "

msg =MIMEText("TEST")
msg['Subject'] = 'Test email'
msg['From'] = sender
msg['To'] = COMMASPACE.join(receivers)


smtp_server = smtplib.SMTP("smtp.163.com", 25)
smtp_server.login(sender, password)
smtp_server.sendmail(sender, receivers, msg.as_string())
