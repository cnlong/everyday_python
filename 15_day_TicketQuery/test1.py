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
    arguments = docopt(__doc__)
    print(arguments)


if __name__ == '__main__':
    cli()