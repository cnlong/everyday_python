import yagmail


password = input("输入密码：")
mail_server = yagmail.SMTP(user="l17625924672@163.com", password=password, host='smtp.163.com', port=587)

content = ['this is the body, and here is just text',
           'you can find an image file and a pdf file attached',
           'test.jpg', 'test.txt']

mail_server.send('long.chen@xiaoyuer.com', 'This mail come from yagmail', content)
mail_server.close()