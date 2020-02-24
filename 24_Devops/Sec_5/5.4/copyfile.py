import shutil


shutil.copy('copyfile.py', 'copyfile2.py')
shutil.copytree('test', 'test3')
shutil.move('copyfile.py', 'copyfile3.py')
shutil.move('copyfile2.py', 'test')