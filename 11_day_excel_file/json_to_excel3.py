import xlwt
import json


with open("numbers.txt", "r", encoding="UTF-8") as f:
    data = json.load(f)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("numbers")
    for index, value in enumerate(data):
        sheet.write(index, 0, value[0])
        sheet.write(index, 1, value[1])
        sheet.write(index, 2, value[2])
    workbook.save("numbers.xls")
