import random
import string


def create_coupon(num, long):
    basestr = string.digits + string.ascii_uppercase
    b = []
    for i in range(num):
        a = ''
        for j in range(long):
            a += random.choice(basestr)
        b.append(a)
    return b


print(create_coupon(5, 10))
