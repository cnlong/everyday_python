from PIL import Image
import os


def modi_img(directory_name, size_x, size_y):
    for filename in os.listdir(directory_name):
        # 分割文件名，返回文件名和文件扩展名的元组，取后缀名进行比较
        if os.path.splitext(filename)[1] == ".jpg" or os.path.splitext(filename)[1] == ".png":
            i = Image.open(directory_name + "/" + filename)
            i_resize = i.resize((size_x, size_y), Image.NEAREST)
            # i_resize.show()
            i_resize.save(directory_name + "/" + filename + "_new.jpg")
            print("%s ok" % filename)


modi_img("IMG", 1136, 640)
