import random

# 随机生成0到1范围之间的一个随机数
print("随机数1:", random.random())
# 在指定范围内生成随机数
print("随机数2:", random.uniform(2, 6))
# 在指定范围内生成随机整数
print("随机数3:", random.randint(6, 8))
# 在指定范围中，按指定基数递增生成的数据集合中随机获得一个数，三个参数，前两个为上下限，第三个为递增增量
print("随机数4:", random.randrange(1, 10, 2))
# 从序列中获取一个随机元素
print("随机元素1:" , random.choice("www.xiaoyuer.com"))
# 将一个列表中的元素打乱，随机排序，列表会被改变
list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print("新列表1:", list1)
# 从指定序列中随机获取指定长度的片段，原有序列不便，第一个参数是指定序列，第二个参数是需要获取的片段长度
num = [1, 2, 3, 4, 5, 6]
a = "abcdefghijk"
print("随机序列1:", random.sample(num, 3))
print("随机序列2:", random.sample(a, 3))