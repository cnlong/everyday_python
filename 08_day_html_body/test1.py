from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建BeautifulSoup对象
# html.parser是Python标准库中的html解析器类型，，不加这个会报警
soup = BeautifulSoup(html, 'html.parser')
# 格式化输出html文件
print(soup.prettify())

print("="*50)
# 找到文档的title
print(soup.title)

print("="*50)
# title的name值
print(soup.title.name)

print("="*50)
# title中的字符串String
print(soup.title.string)

print("="*50)
# title的父亲节点的name属性
print(soup.title.parent.name)

print("="*50)
# 文档的第一个找到的段落
print(soup.p)

print("="*50)
# 找到的p的class属性值
print(soup.p['class'])

print("="*50)
# 找到a标签
print(soup.a)

print("="*50)
# 找到所有的a标签
print(soup.find_all('a'))

print("="*50)
# 找到id值等于3的a标签
print(soup.find(id="link3"))

#我们可以通过get_text 方法 快速得到源文件中的所有text内容。
print(soup.get_text())