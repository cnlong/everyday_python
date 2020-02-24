import shutil
import os
import zipfile

shutil.make_archive('backup', 'gztar')
shutil.make_archive('backup', 'zip')

print(os.listdir('.'))
print("*"*50)

f = zipfile.ZipFile('backup.zip')
for i in f.namelist():
    print(i)

