import zipfile
example_zip = zipfile.ZipFile('example.zip')
for i in example_zip.namelist():
    print(i)

a = example_zip.extract('test1.py')
# print(a)