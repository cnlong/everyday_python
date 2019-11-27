from collections import OrderedDict
import json
import xlwt


with open("student.txt", "r", encoding="UTF-8") as f:
    """
    object_pairs_hook是一个可选参数
    通常这么使用，object_pairs_hook=OrderedDict
    对加载结果进行调用，并返回，返回的不再是dict,而是OrderedDict
    是一个有序字典
    """
    # json.load加载一个读取的json文本对象,并返回一个有序Dict类型
    data = json.load(f, object_pairs_hook=OrderedDict)
    # 创建excel工作簿
    workbook = xlwt.Workbook()
    # 创建excel单张表，第一个参数是表名，第二个表示是否可以复写
    sheet = workbook.add_sheet('student', cell_overwrite_ok=True)
    # data.items()返回的是一个类似列表的dict_items类型，列表元素由字典的键值组成
    # print(data.items())
    # print(list(data.items()))
    # print(type(data.items()))
    # items()函数以列表返回可遍历的键、值
    """   
     enumerate()将一个可遍历的对象组合成一个索引序列对象（枚举对象）
     索引默认从0开始，而索引对应的值就是原可遍历对象的元素
    """
    for index, (key, value) in enumerate(data.items()):
        # print(index, key, value)
        """
        sheet.write(index, 0, key) 即sheet.write("行","列","内容")
        sheet.write(0, 0, key)就是excel表格中的第一行第一列即A1框
        """
        # 遍历索引从所有0开始，每行1列1列的插入
        sheet.write(index, 0, key)
        for i, value2 in enumerate(value):
            # print(index, i+1, value)
            # 根据vlaue值的枚举对象进行遍历，i即为索引，从每行的第二列开始插入
            # 此时后面的value为['张三', 150, 120, 100]
            # 而前面的value2为'张三'或者150或者120或者100
            sheet.write(index, i+1, value2)
    workbook.save("student.xls")