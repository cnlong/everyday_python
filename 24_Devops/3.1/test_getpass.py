import getpass


user = getpass.getuser()
passwd = getpass.getpass('your passwd: ')
input_passwd = input("your input_passwd: ")
print(user, passwd)