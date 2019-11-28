import xlrd


with xlrd.open_workbook("student.xls") as f:
    # 通过sheet名称获取所需的sheet对象
    print(f.sheet_by_name("student"))
    # 通过sheet索引获取所需的sheet对象
    print(f.sheet_by_index(sheetx=0))
    # 获取所有sheet的名称，以列表方式显示
    print(f.sheet_names())
    # 获取所有sheet的对象，以列表形式显示
    print(f.sheets())
    # 获取某sheet中的有效行数
    a = f.sheet_by_index(sheetx=0)
    print(a.nrows)
    # 获取sheet中第一行的数据
    row_values = a.row_values(rowx=1)
    print(row_values)
    row = a.row(1)
    print(row)
    print(row[0].value)
