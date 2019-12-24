import re
import os
import zipfile

"""
# 第一步读取出来的内容是"collect the comments",收集注释信息
# num = re.compile(r"Next nothing is (\d+)")
# start_num = 90052
# while True:
#     file_name = str(start_num) + ".txt"
#     file_path = os.path.join("channel", file_name)
#     with open(file_path, "r") as f:
#         content = f.read()
#     try:
#         next_num = num.match(content)
#         start_num = next_num.group(1)
#     except Exception as e:
#         print(content)
#         break
"""
# 第二步，收集所有文件的注释信息

num = re.compile(r"Next nothing is (\d+)")
start_num = 90052
comments = list()
# 通过zipfile模块读取zip文件信息，返回的是一个zip类,参数"r"是读取
z = zipfile.ZipFile("channel.zip", "r")
while True:
    file_name = str(start_num) + ".txt"
    file_path = os.path.join("channel", file_name)
    # 通过infolist方法以列表形式返回，元素是zip文件中每个文件的详细信息
    # print(z.infolist())
    # 通过getinfo(filename)获取指定文件的信息元素
    file_info = z.getinfo(file_name)
    # 获取注释信息，获取到的是byte，需要进行解码
    comment = file_info.comment.decode()
    comments.append(comment)
    with open(file_path, "r") as f:
        content = f.read()
    try:
        next_num = num.match(content)
        start_num = next_num.group(1)
    except Exception as e:
        print(content)
        break

print("".join(comments))