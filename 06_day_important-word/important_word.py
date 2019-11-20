import os
import collections
"""
这一个版本有个问题，就是文本中的句号或者问号结尾的单词无法准确区分出来，会将同样一个单词，一个带句号一个不带句号，会被区分成两个单词，出现次数统计错误
"""

def important_word(dir_path):
    file_list = os.listdir(dir_path)
    for file_name in file_list:
        with open(dir_path + "/" + file_name, "r", encoding="UTF-8") as f:
            file_content = f.read()
            content_list = file_content.split(" ")
        content_dict = collections.Counter(content_list)
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