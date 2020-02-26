import requests
# Beautiful Soup 是一个用来解析 html 或者 xml 文件的库，支持元素选择器来选择需要的标签
from bs4 import BeautifulSoup
import csv
import lxml

url = "https://nj.58.com/pinpaigongyu/pn/{}/?minprice=1500_2000"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

page = 0

# 创建一个文件用于存储csv数据
csv_file = open("rent.csv", "w")
# 创建一个csv writer对象，设定分隔符为逗号
csv_witer = csv.writer(csv_file, delimiter=",")


# 获取的房源信息的价格会显示成未知的汉字，需要进行转换
def convertNum(char):
    # 汉字列表0-9
    cha_list = ['龤','龒','閏','麣','餼','驋','龥','鑶','鸺','齤']
    num = ""
    for i in char:
        if i == "-":
            num += "-"
            continue
        # 获取汉字在列表中对应的索引，并转为字符串
        num += str(cha_list.index(i))
    return num


while True:
    page += 1
    print("get:", url.format(page))
    response = requests.get(url.format(page), headers=head)
    html = BeautifulSoup(response.text, features="lxml")
    # select选择class为list下的li标签
    house_list = html.select(".list > li")

    for house in house_list:
        # select选择标签为h2的部分，并返回一个list，提取列表中的元素
        # 通过string属性打印出不含标签的文字内容部分，并转换成字符串
        house_title = house.select("h2")[0].string
        # 筛选出a标签，并取出href链接部分
        house_url = house.select("a")[0]["href"]
        house_info_list = house_title.split()
        # 获取地址
        house_location = house_info_list[1]
        # 获取价格
        house_money = house.select(".money")[0].select("b")[0].string
        # 因为获取的字符串中有特殊符号"\r" "\n" " "，在做繁体字转换的时候，会报错，所以先将这些特殊符号替换成空
        house_money = house_money.replace("\r", "")
        house_money = house_money.replace("\n", "")
        house_money = house_money.replace(" ", "")
        house_money = convertNum(house_money)
        #将数据写入到csv编辑器中
        csv_witer.writerow([house_title, house_location, house_money, house_url])
    csv_file.close()


    if page == 1:
        break



