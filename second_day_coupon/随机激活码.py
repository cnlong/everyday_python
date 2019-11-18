import string
import random

def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon


def two_hundred_coupons():
    data = ''
    count = 1
    for i in range(200):
        digit = 12
        data += 'coupon no.' + str(count) + ' ' + coupon_creator(digit) + '\n'
        count += 1
    return data

coupondata = open('coupondata.txt', 'w')
coupondata.write(two_hundred_coupons())
coupondata.close()