import imapclient


imap = imapclient.IMAPClient('imap.163.com', ssl=True)

password = input("请输入密码：")
# 登录
imap.login("l17625924672@163.com", password)
# 获取收件箱
print(imap.list_folders())
# 选择收件箱
print(imap.select_folder(u'INBOX'))


