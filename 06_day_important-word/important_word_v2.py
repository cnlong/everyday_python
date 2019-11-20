import os
import collections
import re
"""
修改版，通过"\b?(\w+)\b?"匹配文档内容，可以将文档中带有标点符号的字母单独匹配出来，便于次数统计
"""


def important_word(dir_path):
    file_list = os.listdir(dir_path)
    # \b表示字母数字与非字母数字的边界，或者是非字母数字与字母数字的边界，不匹配任何实际字符，所以看不到
    # re.compile("正则表达式")，将一个正则规则生成一个对象
    regex = re.compile("\b?(\w+)\b?")
    for file_name in file_list:
        with open(dir_path + "/" + file_name, "r", encoding="UTF-8") as f:
            file_content = f.read()
            # 将上述生成的规则用于匹配文档内容，找出所有符合要求的内容，并生成一个列表
            content_list = regex.findall(file_content)
        content_dict = collections.Counter(content_list)
        # print(a[0])
        num = 0
        max_word = ''
        print(content_dict)
        for key, value in content_dict.items():
            if value > num and len(key) > 2 and key != 'the':
                num = value
                max_word = key
        print("%s的重要的单词是:%s，出现次数是:%s" % (file_name, max_word, num))


if __name__ == '__main__':
    important_word("diary")