"""因为获取的源码文件中价格的繁体字一直变化，猜测是js中做了相关定义，暂时不弄"""

def convertNum(char):
    # 汉字列表0-9
    cha_list = ['龤','龒','閏','麣','餼','驋','龥','鑶','鸺','齤']
    num = ""
    for i in char:
        if i == "-":
            num += "-"
            continue
        # 获取汉字在列表中对应的索引，并转为字符串
        num += str(cha_list.index(i))
    return num

char = "麣閏龒龒-麣鸺龒龒"