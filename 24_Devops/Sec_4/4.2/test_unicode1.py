name = '赖明星'
with open('test.txt', "w") as f:
    f.write(name)

with open('test.txt', "r") as f:
    data = f.read()

print(type(data))
print(type(b'aa'))
print(u'aa')