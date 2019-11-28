import xlrd
import json
import xml.dom.minidom as md


def read_xls(filename):
    with xlrd.open_workbook(filename) as f:
        sheet = f.sheet_by_index(sheetx=0)
        lines = sheet.nrows
        data = dict()
        for i in range(lines):
            row_values = sheet.row_values(i)
            data[row_values[0]] = row_values[1:]
    return data


def city_xml(data):
    xmlfile = md.Document()
    root = xmlfile.createElement('root')
    cities = xmlfile.createElement('cities')
    xmlfile.appendChild(root)
    root.appendChild(cities)
    comment = xmlfile.createComment('城市信息')
    cities.appendChild(comment)
    xmlcontent = xmlfile.createTextNode(str(data))
    cities.appendChild(xmlcontent)
    with open('city.xml ', "wb") as f:
        f.write(xmlfile.toprettyxml(encoding="UTF-8"))

def numbers_xml(data):
    xmlfile = md.Document()
    root = xmlfile.createElement('root')
    numbers = xmlfile.createElement('numbers')
    xmlfile.appendChild(root)
    root.appendChild(numbers)
    comment = xmlfile.createComment('数字信息')
    numbers.appendChild(comment)
    xmlcontent = xmlfile.createTextNode(str(data))
    numbers.appendChild(xmlcontent)
    with open('numbers.xml ', "wb") as f:
        f.write(xmlfile.toprettyxml(encoding="UTF-8"))


city_xml(read_xls("city.xls"))
numbers_xml(read_xls("numbers.xls"))