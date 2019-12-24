import re
import zipfile
import os


num = 7331
file_name = str(num) + ".txt"
file_path = os.path.join("channel", file_name)
# a = "Next nothing is 226"
# b = num.match(a)

z = zipfile.ZipFile("channel.zip", "r")
print(z.infolist())
print((z.getinfo(file_name)))
print(z.read(file_name))
