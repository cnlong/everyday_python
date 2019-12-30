#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time


source = ["/root/cmake-2.8.11.2/"]
target_dir = "/root/backup/"

# time.strftime('%Y%m%d%H%M%S')将时间元组或 struct_time 对象格式化为指定格式的时间字符串。
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# linux中zip压缩的命令
zip_command = "zip -qr %s %s" % (target, " ".join(source))


# 将字符串转化成命令在服务器上运行；其原理是每一条system函数执行时，其会创建一个子进程在系统上执行命令行，子进程的执行结果无法影响主进程
# 返回值为0表示执行成功，其他值则执行失败
if os.system(zip_command) == 0:
    print("Successfule Backup")
else:
    print("Failed Backup")


