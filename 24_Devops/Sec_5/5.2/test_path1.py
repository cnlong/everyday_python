import os


print('currrent directory: ', os.getcwd())
path = os.path.abspath(__file__)
print("full path of current file: ", path)
print("parent directory of current file: ",
      os.path.abspath(os.path.join(os.path.dirname(path), os.path.pardir)))
print(os.path.join(os.path.dirname(path), os.path.pardir))

