import os
import collections
import re
"""
修改版，通过"\b?(\w+)\b?"匹配文档内容，可以将文档中带有标点符号的字母单独匹配出来，便于次数统计
另外常用的"is"、"we"、"the"等单词，可以通过新建一个新的字典，判断key值，将不是这些单词的Key value新增到字典中
"""


def important_word(dir_path):
    file_list = os.listdir(dir_path)
    regex = re.compile("\b?(\w+)\b?")
    for file_name in file_list:
        with open(dir_path + "/" + file_name, "r", encoding="UTF-8") as f:
            file_content = f.read()
            content_list = regex.findall(file_content)
        content_dict = collections.Counter(content_list)
        # Counter排序，对字典中的词按值排降序，会返回一个由许多元组所组成的列表，按值的大小依次降序排列
        a = collections.Counter.most_common(content_dict)
        # 或者使用sorted内建函数对可迭代对象进行排序
        # b = sorted(content_dict.items(), key=lambda x: x[1], reverse=True)
        # print(b)
        print("出现最多的单词是:%s,出现次数是:%s" % (a[1][0], a[1][1]))


if __name__ == '__main__':
    important_word("diary")