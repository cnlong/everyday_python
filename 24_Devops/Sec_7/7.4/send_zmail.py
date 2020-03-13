import zmail

mail = {
    'subject': '这是一份测试邮件的标题',
    'content_text': '测试邮件的正文内容',
    # 添加附件
    'attachments': ['test.jpg', 'test.txt']
}

# 连接邮箱
password = input("请输入密码：")
server = zmail.server("l17625924672@163.com", password)
receivers = ['271138425@qq.com', 'long.chen@xiaoyuer.com']
server.send_mail(receivers, mail)