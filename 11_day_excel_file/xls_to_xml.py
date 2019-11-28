import xlrd
import xml.dom.minidom as md


# 使用xlrd读取excel表格，读取出来的是一个xlrd对象
with xlrd.open_workbook("student.xls") as data:
    # 获取名称为student的sheet对象
    stu_sheet = data.sheet_by_name("student")
    # 获取该sheet的行数
    lines = stu_sheet.nrows
    # 遍历每一行数据，组成新字典
    data = dict()
    value_list = list()
    for i in range(lines):
        # 获取每一行的数据
        row_values = stu_sheet.row_values(i)
        data[row_values[0]] = row_values[1:]
    # 创建新xml文件
    xmlfile = md.Document()
    # 创建节点
    root = xmlfile.createElement('root')
    students = xmlfile.createElement('students')
    # 在文件中添加root节点
    xmlfile.appendChild(root)
    # 在root节点下添加student节点
    root.appendChild(students)
    # 创建评论
    comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')
    # 在students标签下添加comment
    students.appendChild(comment)
    # 创建文本节点
    xmlcontent = xmlfile.createTextNode(str(data))
    # 在students标签下添加文本内容
    students.appendChild(xmlcontent)
    """
    将xml写入文件
    xmlfile是xml类型对象，需要对其进行转变，转换成xml
    可以使用writexml或者toprettyxml
    第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
    第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
    以"w"方式为报错，需要改为"wb"
    Python3给open函数添加了名为encoding的新参数，而这个新参数的默认值却是‘utf-8’。这样在文件句柄上进行read和write操作时，系统就要求开发者必须传入包含Unicode字符的实例，而不接受包含二进制数据的bytes实例。
    """
    with open("student.xml", "wb") as f:
        f.write(xmlfile.toprettyxml(encoding="UTF-8"))

