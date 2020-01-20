import os
from collections import Counter


c = Counter()
# print(os.path.expanduser('~/.bash_history'))
# os.path.expanduser('~/.bash_history')能够直接解析"~"获取用户家目录
with open(os.path.expanduser('~/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]] += 1


print(c.most_common(10))