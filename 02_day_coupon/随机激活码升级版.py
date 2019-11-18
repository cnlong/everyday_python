import random
import string


class Coupon(object):
    def __init__(self, num, length, file):
        self.num = num
        self.length = length
        self.file = file

    def creator(self):
        coupondata = ''
        for i in range(self.length):
            coupondata += random.choice(string.ascii_uppercase+string.digits)
        # print(coupondata)
        return coupondata

    def coupon_store(self):
        data = ''
        count = 1
        for i in range(self.num):
            data += 'coupon no.' + str(count) + ':' + self.creator() + '\n'
            count += 1
        # print(data)
        coupontxt = open(self.file, "w")
        coupontxt.write(data)
        coupontxt.close()
        print("生成激活码成功:%s" % self.file)


if __name__ == '__main__':
    num = int(input("输入激活码数量:"))
    length = int(input("输入激活码长度:"))
    filename = input("输入激活码文件名称:")
    coupon = Coupon(num, length, filename)
    coupon.coupon_store()