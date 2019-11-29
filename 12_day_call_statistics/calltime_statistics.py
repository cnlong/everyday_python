import xlrd
import re
from functools import reduce


with xlrd.open_workbook("call.xls") as data:
    sheet = data.sheet_by_index(sheetx=0)
    # 获取第5+1列的第7+1行到330+1行的数据，返回的是一个列表
    call_list = sheet.col_values(colx=5, start_rowx=7, end_rowx=330)
    hour_list = list()
    min_list = list()
    sec_list = list()
    for i in call_list:
        ret = re.findall(r"\d+", i)
        if len(ret) == 1:
            sec_list.append(int(ret[0]))
        if len(ret) == 2:
            min_list.append(int(ret[0]))
            sec_list.append(int(ret[1]))
        if len(ret) == 3:
            hour_list.append(int(ret[0]))
            min_list.append(int(ret[1]))
            sec_list.append(int(ret[2]))
    # min_num = sum(min_list)
    # sec_num = sum(sec_list)
    hour_num = sum(hour_list)
    min_num = reduce(lambda x, y:x+y, min_list)
    sec_num = reduce(lambda x, y:x+y, sec_list)
    time_num = hour_num*3600 + min_num*60+sec_num
    print("总时长：%s秒" % time_num)
    hours = (time_num//3600 )
    mins = ((time_num%3600)//60)
    print("总时长：%s时%s分" % (hours, mins))

