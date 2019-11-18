import random
import string
import pymysql


class Coupon(object):
    def __init__(self, num, length, file):
        self.num = num
        self.length = length
        self.file = file

    def coupon_store(self):
        data = []
        count = 1
        for i in range(self.num):
            # coupon的内容每次循环需要清空，不然会被下次调用
            coupon = ''
            for j in range(self.length):
                coupon += random.choice(string.ascii_uppercase + string.digits)
            data.append(coupon)
            count += 1
        # print(data)
        coupontxt = open(self.file, "w")
        coupontxt.write(str(data))
        coupontxt.close()
        print("生成激活码成功:%s" % self.file)
        return data


    def InsertIntoMysql(self):
        coon = pymysql.connect(host='192.168.6.166', port=3306, user='root', passwd='123456', database='python_practise', charset='utf8')
        cur = coon.cursor()
        coupondata = self.coupon_store()
        data_list = list()
        for i in coupondata:
            data_list.append("""'%s'""" % i)
        for i in data_list:
            cur.execute('insert into coupondata (coupon) values (%s);' % i)
            coon.commit()
        cur.close()
        coon.close()
        print("写入数据库成功！")


if __name__ == '__main__':
    num = int(input("输入激活码数量:"))
    length = int(input("输入激活码长度:"))
    filename = input("输入激活码文件名称:")
    coupon = Coupon(num, length, filename)
    # coupon.coupon_store()
    coupon.InsertIntoMysql()