import pickle


with open("banner.p", "rb") as f:
    content = f.read()

# 将序列号存储的数据转化为python对象
data = pickle.loads(content)
# 读取对象，找出规则
# 返回的列表中的包含多个子列表，子列表中由多个元组组成
# 单个子列表打印，发现类似于一个文档每一行，字符按顺序出现的次数
# for i in data:
#     print(i)

# 组合打印
for i in data:
    # print([a[0] * a[1] for a in i ])
    print("".join([a[0] * a[1] for a in i ]))