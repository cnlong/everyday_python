import os
from bs4 import BeautifulSoup

def body_extraction(dirpath):
    filelist = os.listdir(dirpath)
    for i in filelist:
        filename = os.path.join(dirpath, i)
        with open(filename, "r", encoding="UTF-8") as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        # 获取所有的正文内容
        content = soup.get_text()
        print(content)
        # 获取超链接
        urls = soup.find_all('a')
        for i in urls:
            print(i)


if __name__ == '__main__':
    body_extraction("html")