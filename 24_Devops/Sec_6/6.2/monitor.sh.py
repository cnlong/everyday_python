# namedtuple可以不用通过索引值进行访问，可以根据字典的key方式来访问，但是其值不能改变
from collections import namedtuple
import sys


Disk = namedtuple('Disk', 'major_number minor_number device_name '
                          'read_count read_merged_count read_sections '
                          'time_spent_reading write_count write_merged_count '
                          'write_sections time_spent_write io_requests '
                          'time_spent_doing_io weighted_time_spent_doing_io')


def get_disk_info(device):
    """
    获取磁盘信息
    :param device: 磁盘名称
    :return: 返回磁盘的信息
    """
    with open("/proc/diskstats") as f:
        for line in f:
            # 找到指定的磁盘
            if line.split()[2] == device:
                # 将信息一一传入到namedtuple中
                return Disk(*(line.split()))
    # 如果找不到对应的磁盘信息，抛出一般的运行时错误
    raise RuntimeError("device {0} not found".format(device))


def main():
    sys.argv.append("")
    disk = sys.argv[1]
    disk_info = get_disk_info(disk)
    print("磁盘写次数：{0}".format(disk_info.write_count))
    print("磁盘写延时：{0}".format(disk_info.time_spent_write))


if __name__ == '__main__':
    main()


