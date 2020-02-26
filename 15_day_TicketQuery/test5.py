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
from prettytable import PrettyTable
from colorama import init, Fore


# 颜色模块初始化
init()
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9125"
res = requests.get(url)
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', res.text)
stations = dict(stations)
stations_two = dict()
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

    @property
    def infotrains(self):
        for i in self.avaliale_trains:
            each_train_list = i.split('|')
            train_code = each_train_list[3]
            if not self.options or train_code[0].lower() in self.options:
                # 给字体输出加颜色
                # Fore.BLUE：定义颜色
                # Fore.RESET：设定该颜色渲染终止
                trains = [Fore.BLUE+train_code+Fore.RESET,
                          Fore.RED+stations_two[each_train_list[6]]+Fore.RESET,  # 出发站台信息
                          Fore.GREEN+stations_two[each_train_list[7]]+Fore.RESET,  # 到达站台信息
                          Fore.RED+each_train_list[8]+Fore.RESET,  # 发车时间
                          Fore.GREEN+each_train_list[9]+Fore.RESET,  # 到达时间
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
                # 通过yield将此函数变为生成器，每次循环遍历返回一个值，下次接着上次的状态继续循环遍历，而不是重新执行函数
                yield trains

    def print_train_info(self):
        # 创建表格对象
        tb = PrettyTable()
        # 添加表头信息
        tb.field_names = ["车次", "出发站台", "到达站台", "发车时间", "到达时间", "时长(h)", "站票", "硬座", "软座", "硬卧", "动卧", "软卧", "高级软卧", "二等座", "一等座", "特等座", "商务座", "其他"]
        """for 循环遍历生成器的过程：
            1.判断遍历的对象是否有__iter__函数方法
            2.获取__iter__函数返回的结果，且其返回的结果是一个迭代器（同时包含__iter__和__next__方法的对象）
            3.通过返回结果迭代器的netx方法取出值交给循环参数tranis,然后执行后续的循环体
            4.因为需要不断循环遍历出不同的结果，所以需要上一个函数变为生成器，记住每次取值的状态，用于迭代循环
        """
        for train in self.infotrains:
            # 将返回出来的车次信息列表添加到表格中
            tb.add_row(train)
        print(tb)


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
    options = "".join([x for x, y in arguments.items() if y is True])
    trainsinfo = TrainsInfo(available_trains, options)
    trainsinfo.print_train_info()


if __name__ == '__main__':
    cli()