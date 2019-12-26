# from PIL import Image
#
#
# with open("test-data/set1/img-0.png", "rb") as f:
#     img = Image.open(f)
#     img.load()
# npixels = img.size[0] * img.size[1]
# cols = img.getcolors()
# print(cols)
a = float('inf')
print(type(a))

# 获取列表元素的索引
a = [1, 2, 3, 4, 5]
for i in a:
    print("%s的索引是%s" % (i, a.index(i)))

b = enumerate(a)
print(list(b))

print(int(0.2))