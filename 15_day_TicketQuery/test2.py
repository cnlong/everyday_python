"""
浏览器查询火车票的请求过程：
1.发送请求，请求中带入出发地目的地日期，发送
2.出发地目的地会 转换成英文代码进行发送
3.根据返回数据获得查询情况
"""
import re, requests
# 输出美化模块
from pprint import pprint
import json


# 从浏览器中找到中英文对照表的URL
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9125"
# 使用requests库发起请求，获得响应的json文件
res = requests.get(url)
# '\u4e00'将unicode编码转为中文
# 中文的unicode一般编码范围是4e00-9fa5（或者4E00-9FA5）
# 正则匹配文件内容中符合这个规则，类似"(北京)|(VAP)"，匹配到组成列表返回，列表的每个元素是一个元组，包含规则中匹配到的两个符合要求的字符
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', res.text)
# 将返回列表转成字典，格式化输出，indent参数代表缩进
# 格式化输出列表没有字典看的舒服
pprint(dict(stations), indent=4)
head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'JSESSIONID=38D584127A74B2C708875827108DBB12; BIGipServerotn=435159562.38945.0000; RAIL_EXPIRATION=1575766157251; RAIL_DEVICEID=jQps1RWlcrbnVc67YsBTVc3u0vgvNXDYK2Uo6vLZCEBhC6tbq5R6DSvDuV54nI0Ca1Ht3LUVUvb5UKvj1Be8Q9RHv22tQBq2uDPgoEBrax1hDsnD9CT_kiB2_GObLAjlf6st2RlD06qxXNkV3GMB_nWHyRvxfgSo; BIGipServerpool_passport=200081930.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2019-12-04; _jc_save_toDate=2019-12-04; _jc_save_wfdc_flag=dc',
'Host':'kyfw.12306.cn',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-12-05&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
ret = requests.get(url, headers=head)
print(ret.json()['data']['result'])
