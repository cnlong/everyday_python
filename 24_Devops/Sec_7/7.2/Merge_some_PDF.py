"""
合并多个文件
"""
import PyPDF2


# 创建一个Merge类
merger = PyPDF2.PdfFileMerger()

input1 = open("redbook.pdf", 'rb')
input2 = open("redbook.pdf", 'rb')
input3 = open("redbook.pdf", 'rb')

# 将input1的前三页添加到merger中
merger.append(fileobj=input1, pages=(0, 3))

# 再将input2的前两页指定从第二个位置插入,会覆盖之前添加的第三页
merger.merge(position=2, fileobj=input2, pages=(0, 1))

# 再将input3添加到尾部
merger.append(fileobj=input3, pages=(0,10))

# 保存
with open("document-output.pdf", 'wb') as f:
    merger.write(f)