命令行邮件客户端
发送邮件的时候需要输入以下信息：
1.SMTP服务器的域名
2.SMTP服务器的端口号
3.登录SMTP服务器的用户名
4.登录SMTP服务器的密码
5.邮件的主题
6.邮件的内容
7.邮件的附件
8.邮件的收件人

SMTP相关的配置作为配置文件内容

longmail.py可改进之处：
1.参数获取可以使用doct，更为直观
2.配置文件可以指定默认，无需每次手动指定


安装python包的两种方式：
	*
源码包下面执行，python setup.py install
	*
pip install 包/ easy_install 包

生成tar包 python setup.py sdist

