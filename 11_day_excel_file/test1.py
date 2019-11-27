data = {'1': ['张三', 150, 120, 100], '2': ['李四', 90, 99, 95], '3': ['王五', 60, 66, 68]}
a = enumerate(data.items())
print(a)
for index, (key, value) in a:
    print(index, (key, value))