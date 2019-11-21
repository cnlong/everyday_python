import os
import re


def code_statistic(dirpath):
    file_list = os.listdir(dirpath)
    for filename in file_list:
        with open(dirpath + "/" + filename, "r", encoding="UTF-8") as f:
            content = f.readlines()
        comments = list()
        blank = list()
        codelines = list()
        for i in content:
            if re.match(r"(\s)*#.*?", i):
                comments.append(i)
            if re.match(r"(\n).*?", i):
                blank.append(i)
            if re.match(r"(\s)*(\w)+", i):
                codelines.append(i)
        print("%s的代码行数为:%s" % (filename, len(content)))
        print("空行行数为:%s" % (len(blank)))
        print("代码行数为:%s" % (len(codelines)))
        print("注释行数为:%s" % (len(comments)))


if __name__ == '__main__':
    code_statistic("code")