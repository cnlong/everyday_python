import PyPDF2


reader = PyPDF2.PdfFileReader(open('redbook.pdf', 'rb'))

# 获取文档页数
print(reader.getNumPages())

# 验证是否加密
print(reader.getIsEncrypted())

# 获取第5页
page = reader.getPage(4)

# 提取第5页的内容
print(page.extractText)

# 获取PDF文件的元信息，返回一个字典，保存了PDF文件的描述以及取值
print(reader.getDocumentInfo())