from PIL import Image
import os.path

def Size(dirPath, size_x, size_y):
    f = os.listdir(dirPath)
    for i in f:
        # 分割文件名，返回文件名和文件扩展名的元组，取后缀名进行比较
        if os.path.splitext(i)[1] == ".jpg" or os.path.splitext(i)[1] == ".png":
            img = Image.open(dirPath + "/" + i)
            img_resize = img.resize((size_x, size_y), Image.NEAREST)
            img_resize.save(dirPath + "/" + i + "_new1.jpg")


Size("IMG", 1136, 640)