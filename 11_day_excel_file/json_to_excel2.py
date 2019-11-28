from collections import OrderedDict
import xlwt
import json


with open("city.txt", "r", encoding="UTF-8") as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("city")
    for index, (key, value) in enumerate(data.items()):
        sheet.write(index, 0, key)
        sheet.write(index, 1, value)
    workbook.save("city.xls")
