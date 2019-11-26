import re
with open("filtered_words.txt", "r", encoding="UTF-8") as f:
    data = f.read().splitlines()
a = str(input("请输入："))
for i in data:
    if i in a:
        a = re.sub(i, "*"*len(i), a)
print(a)