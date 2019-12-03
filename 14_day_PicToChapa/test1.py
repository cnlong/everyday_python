from PIL import Image
import os


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=0):
    if alpha == 0:
        return " "
    # 获取字符集的长度
    length = len(ascii_char)
    # 将RGB值转换为灰度值gray,灰度值范围0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 将灰度值对应到列表中的字符
    unit = (256+1)/length
    # 获取灰度值对应的字符串
    return ascii_char[int(gray/unit)]


def PicToCha(dir_path):
    file_list = os.listdir(dir_path)
    for file in file_list:
        # 将文件名和目录名合并
        file_path = os.path.join(dir_path, file)
        with open(file_path, 'rb') as f:
            im = Image.open(f)
            im = im.resize((50, 50), Image.NEAREST)
            width, height = im.size
            text = ''
            for i in range(height):
                for j in range(width):
                    # 通过图片每个像素点的RGB值获取对应的字符
                    text += get_char(*im.getpixel((j, i)))
                text += "\n"
            print(text)
        with open(file + ".txt", "w") as f:
            f.write(text)


if __name__ == '__main__':
    PicToCha("IMG")