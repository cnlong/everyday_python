from PIL import Image,ImageDraw,ImageFont


def add_num(img, num):
    # 创建绘画对象
    draw = ImageDraw.Draw(img)
    # 创建字体对象
    myfont = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', size=50)
    # 颜色
    fillcolor = "red"
    # 获取图片长宽
    width, height = img.size
    # 绘画对象调用text()方法添加文字,（位置,文字,字体,颜色）
    draw.text((width-90, 0), str(num), font=myfont, fill=fillcolor)
    # 保存图片(文件名, 格式)
    img.save('result-小胖.jpg', 'jpeg')
    a = Image.open('result-小胖.jpg', 'r')
    # 展示图片
    a.show()


if __name__ == '__main__':
    # 创建图片对象
    image = Image.open('小胖.jpg')
    add_num(image, "131")