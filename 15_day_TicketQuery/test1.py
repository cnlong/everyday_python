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

def cli():
    # 返回的是一个字典，键为Usage和Options中选项，值为实际输入内容。
    # 例如tickets 杭州 北京 2019-10-01
    # "杭州" -> "<from>"
    # "北京" -> "<to>"
    # "2019-10-01" -> "<date>"
    # dict_items([('-g', False), ('-d', False), ('-t', False), ('-k', False), ('-z', False), ('<from>', '南京'), ('<to>', '沧州'), ('<date>', '2019-12-10')])
    arguments = docopt(__doc__)
    # print(arguments.items())
    options = "".join([key for key, value in arguments.items() if value == True])
    print(options)
    # "-g-d-z"


if __name__ == '__main__':
    cli()