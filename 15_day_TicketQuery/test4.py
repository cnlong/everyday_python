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


url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9125"
res = requests.get(url)
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', res.text)
stations = dict(stations)
stations_two = dict()
# 颠倒站台代码信息表，能够从代码获取中文站台名称
for key, value in stations.items():
    stations_two[value] = key


class TrainsInfo:
    """处理提取出来的车次信息的类"""
    def __init__(self, avaliable_trains, options):
        """
        车次信息
        :param avaliable_trains: 提取出来总的车次信息
        :param options: 车型，高铁、动车等
        """
        self.avaliale_trains = avaliable_trains
        self.options = options

    # property装饰器使得被装饰的函数能够像属性一样调用
    @property
    def infotrains(self):
        for i in self.avaliale_trains:
            # 返回的车次信息列表中，每一个元素都由"|"分隔的字符串
            # 通过split函数将其分隔成列表，便于取出对应的元素
            each_train_list = i.split('|')
            train_code = each_train_list[3]
            # 需要根据车型参数选项获取对应的车次信息
            # 动车只筛选动车，高铁只筛选高铁
            # 未填入车型选项默认输出
            # 或者填入了选项，只有车次信息的首字母包含在传入的车型选项中才输出
            if not self.options or train_code[0].lower() in self.options:
                trains = [train_code,
                          stations_two[each_train_list[6]],  # 出发站台信息
                          stations_two[each_train_list[7]],  # 到达站台信息
                          each_train_list[8],  # 发车信息
                          each_train_list[9],  # 发车信息
                          each_train_list[10],  # 时长
                          each_train_list[26] if each_train_list[26] else '--',  # 站票信息，没有则显示"--"
                          each_train_list[27] if each_train_list[27] else '--',  # 硬座信息，没有则显示"--"
                          each_train_list[24] if each_train_list[24] else '--',  # 软座信息，没有则显示"--"
                          each_train_list[28] if each_train_list[28] else '--',  # 硬卧信息，没有则显示"--"
                          each_train_list[33] if each_train_list[33] else '--',  # 动卧信息，没有则显示"--"
                          each_train_list[23] if each_train_list[23] else '--',  # 软卧信息，没有则显示"--"
                          each_train_list[21] if each_train_list[21] else '--',  # 高级软卧信息，没有则显示"--"
                          each_train_list[30] if each_train_list[30] else '--',  # 二等座信息，没有则显示"--"
                          each_train_list[31] if each_train_list[31] else '--',  # 一等座信息，没有则显示"--"
                          each_train_list[25] if each_train_list[25] else '--',  # 特等座信息，没有则显示"--"
                          each_train_list[32] if each_train_list[32] else '--',  # 商务座信息，没有则显示"--"
                          each_train_list[22] if each_train_list[22] else '--',  # 其他信息，没有则显示"--"
                          ]
                # 如果这边return的话，直接返回的是提取出来车次信息字典中符合要求的第一个车次信息列表，后续其他符合要求的车次信息就无法输出了
                # 所以这里需要建立一个生成器，通过for循环（或者next）遍历获取所有符合要求的车次信息
                # return trains
                yield trains

    def print_train_info(self):
        for train in self.infotrains:
            print(train)


def cli():
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    head = {
        'Cookie': 'JSESSIONID=38D584127A74B2C708875827108DBB12; BIGipServerotn=435159562.38945.0000; RAIL_EXPIRATION=1575766157251; RAIL_DEVICEID=jQps1RWlcrbnVc67YsBTVc3u0vgvNXDYK2Uo6vLZCEBhC6tbq5R6DSvDuV54nI0Ca1Ht3LUVUvb5UKvj1Be8Q9RHv22tQBq2uDPgoEBrax1hDsnD9CT_kiB2_GObLAjlf6st2RlD06qxXNkV3GMB_nWHyRvxfgSo; BIGipServerpool_passport=200081930.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2019-12-04; _jc_save_toDate=2019-12-04; _jc_save_wfdc_flag=dc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)
    ret = requests.get(url, headers=head)
    available_trains = ret.json()['data']['result']
    # 获取命令行中输入的车型选项参数，如果输入了，则其在grguments字典中对应的值是True
    # 获取车型参数组成的列表，并将其元素合并成字符串，便于作为数据处理类的参数
    options = "".join([x for x, y in arguments.items() if y is True])
    trainsinfo = TrainsInfo(available_trains, options)
    trainsinfo.print_train_info()


if __name__ == '__main__':
    cli()