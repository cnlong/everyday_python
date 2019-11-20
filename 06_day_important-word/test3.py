from collections import Counter
import re
import string
import os


def get_word(txtFile):
    '''
    从一个txt文件中找出出现次数最高的词及其对应次数，以元组形式返回
    '''
    # 过滤词
    stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this', 's', 'is', 'are', 'a', 'with', 'as', 'an']

    f = open(txtFile, 'r', encoding="UTF-8")
    content = f.read().lower()

    pat = '[a-z0-9\']+'
    words = re.findall(pat, content)
    wordList = Counter(words)
    for i in stop_word:
        wordList[i] = 0

    f.close()
    return wordList.most_common()[0]


def traverseFile(path):
    '''
    遍历路径文件夹中的所有文件，并调用get_word函数，输出统计结果
    '''
    for txtName in os.listdir(path):
        txtFile = os.path.join(path, txtName)
        # 调用get_word函数
        most_important = get_word(txtFile)
        print(most_important[0] + ' is the most important word in the essay:' + txtName)
        print('the using times of ' + most_important[0] + " is:" + repr(most_important[1]))
        print("")


if __name__ == "__main__":
    traverseFile(r'diary')
