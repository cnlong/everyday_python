import string
from collections import Counter


with open("message.txt", "r") as f:
    content = f.read()


s = ''
for i in content:
    if i in string.ascii_letters:
        s += i

print(s)


