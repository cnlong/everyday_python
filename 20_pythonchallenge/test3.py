import re


with open("message2.txt", "r") as f:
    content = f.read()

a = re.findall(r"[a-z]+([A-Z]{3}[a-z]{1}[A-Z]{3})[a-z]+", content)
s = ''
for i in a:
    s += i[3]
print(s)