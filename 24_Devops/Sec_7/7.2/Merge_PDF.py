import PyPDF2


reader = PyPDF2.PdfFileReader(open('redbook.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()

for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    # 合并生成一个新的页面
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)

with open('watermark-test.pdf', 'wb') as f:
    writer.write(f)

