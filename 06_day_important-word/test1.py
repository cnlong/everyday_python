import collections
import os.path
def judgeit(words):
    for i in range(6):
        if len(words[i]) > 2 and words[i] != 'the' and words[i] != 'her' and words[i] !=  'his' and words[i] != 'and' and words[i] != 'she':
            return  words[i]
    return words[7]

def mainKeywords(dirPath):
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.txt':
            print('the keywords of' + i + ' is:' )
            with open(dirPath + "/" + i, 'r', encoding="UTF-8") as fp:
                str1 = fp.read().split(' ')
            b = collections.Counter(str1)
            # print(b)
            keywords = sorted(b, key=lambda x: b[x],reverse = True)
            print(keywords)
            print(judgeit(keywords))

mainKeywords("diary")
