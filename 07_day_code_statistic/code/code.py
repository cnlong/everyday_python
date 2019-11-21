import random
import string
import pymysql


def create_coupon(num, long):
    basestr = string.digits + string.ascii_uppercase
    b = []
    for i in range(num):
        a = ''
        for j in range(long):
            a += random.choice(basestr)
        b.append(a)
    return b


def InsertIntoMysql(data):
    # 创建数据库连接
    coon = pymysql.connect(host='192.168.6.166', port=3306, user='root', passwd='123456', database='python_practise', charset='utf8')
    # 创建游标对象
    cur = coon.cursor()
    data_list = list()
    # 因为mysql插入的时候value值需要加引号才能正确插入
    for i in data:
        # print(i)
        if isinstance(i, str):
            data_list.append("""'%s'""" % i)
    # print(data_list)
    for i in data_list:
        print(i)
        cur.execute('insert into coupondata (coupon) values (%s);' % i)
        coon.commit()
    cur.close()
    coon.close()



# print(create_coupon(5, 10))
InsertIntoMysql(create_coupon(5, 10))