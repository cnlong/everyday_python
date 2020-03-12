import PyPDF2


# 打开文件
reader = PyPDF2.PdfFileReader(open('redbook.pdf', 'rb'))
# 新建一个写入对象
output = PyPDF2.PdfFileWriter()
# 向其中添加读取的文件中的2、5、6页
output.addPage(reader.getPage(1))
output.addPage(reader.getPage(4))
output.addPage(reader.getPage(5))
output.encrypt('123456')
# 将新的文件保存
with open("PyPDF2-output.pdf", "wb") as f:
    # PdfFileWriter对象的write方法接收一个以二进制方式打开的文件
    output.write(f)