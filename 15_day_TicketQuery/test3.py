"""
火车票查看器
Usage:
  tickets [-gdtkz] <from> <to> <date>

Options:
  -h,--help     显示帮助信息
  -g            高铁
  -d            动车
  -t            特快
  -k            快速
  -z            直达

Example:
  tickets 杭州 北京 2019-10-01
  tickets -dg 杭州 北京 2019-10-01
"""
from docopt import docopt
import re
import requests
import json


url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9125"
res = requests.get(url)
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', res.text)
stations = dict(stations)


def cli():
    arguments = docopt(__doc__)
    # 返回的是一个字典，键为Usage和Options中选项，值为实际输入内容。
    # 根据命令行输入的起始车站、出发车站查询字典中保存的对应的英文代码
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    # 获取查询请求的URL.并发对应的车站、日期替换成用户输入的信息
    # 请求中必须加入headers，否则获取到的数据和浏览器访问不一样，有反爬虫机制
    # headers中必须要加入Cookie，否则会被限制访问
    # User_Agent，不加的时候返还数据较慢
    head = {
        'Cookie': 'JSESSIONID=38D584127A74B2C708875827108DBB12; BIGipServerotn=435159562.38945.0000; RAIL_EXPIRATION=1575766157251; RAIL_DEVICEID=jQps1RWlcrbnVc67YsBTVc3u0vgvNXDYK2Uo6vLZCEBhC6tbq5R6DSvDuV54nI0Ca1Ht3LUVUvb5UKvj1Be8Q9RHv22tQBq2uDPgoEBrax1hDsnD9CT_kiB2_GObLAjlf6st2RlD06qxXNkV3GMB_nWHyRvxfgSo; BIGipServerpool_passport=200081930.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2019-12-04; _jc_save_toDate=2019-12-04; _jc_save_wfdc_flag=dc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
    ret = requests.get(url, headers=head)
    # 将返回的json文件通过json()方法转成字典
    # 返回的是一个嵌套字典，{'data':{'flag':'xx','map':'xx','result':''}}
    # 车次信息就存储在result中
    # 车次信息存储的数据格式才js源代码中保存，根据对应存储格式获得字段对应的信息类型
    available_trains = ret.json()['data']['result']
    print(available_trains)


if __name__ == '__main__':
    cli()