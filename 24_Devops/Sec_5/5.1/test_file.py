"""
实例：将文本中的所有单词的首字母大写
"""


with open('data.txt') as inf, open('out.txt', 'w') as outf:
    # for line in inf:
    #     outf.write(" ".join([word.capitalize() for word in line.split()]))
    # 需添加换行符，不然新添的字符连接在一起
    #     outf.write('\n')
    for line in inf:
        # print默认自带换行
        print(*[word.capitalize() for word in line.split()], file=outf)