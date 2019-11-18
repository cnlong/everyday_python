import re
import collections

with open('test.txt', 'r') as f:
    content = f.read()

print(content)
a = re.split(r" ", str(content))
b = collections.Counter(a)
for key, value in b.items():
    print("%s:%s" % (key, value))