import collections

with open("test.txt", "r") as f:
    # 英文文档，空格切割文档内容，并返回一个列表
    str = f.read().split(' ')
    # print(str)

# 使用Counter计数器统计列表中字符出现次数
b = collections.Counter(str)
# Counter返回一个Counter类型字典，可以迭代取数据
for key, value in b.items():
    print("%s出现次数:%s" % (key,value))