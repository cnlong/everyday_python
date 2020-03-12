import PyPDF2


reader = PyPDF2.PdfFileReader(open('redbook.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()
page = reader.getPage(0)
# 将页面旋转180度
page.rotateClockwise(180)
writer.addPage(page)
with open("rotata-page-test.pdf", 'wb') as f:
    writer.write(f)


