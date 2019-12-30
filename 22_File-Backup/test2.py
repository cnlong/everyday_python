import os
import time

# 备份的文件目录
source = ["/root/cmake-2.8.11.2/"]
# 备份文件的存储目录
target_dir = "/root/backup/"

# 每天的备份目录
today_dir = target_dir + time.strftime('%Y%m%d')
# 每个时间的备份文件名
time_fielname = time.strftime('%H%M%S')

# os.sep根据你所处的平台，自动采用相应的分隔符号,Windows上，文件的路径分隔符是'\'，在Linux上是'/'
back = today_dir + os.sep + time_fielname + '.zip'
command = "zip -qr {} {}".format(back, " ".join(source))

if not os.path.exists(today_dir):
    print("Mkdir DIR!")
    os.mkdir(today_dir)
if os.system(command)==0:
    print("Successful Backup!")
else:
    print("Failed Backup!")

