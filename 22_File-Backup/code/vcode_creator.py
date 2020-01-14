from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string


class VCodeCreator(object):
    def __init__(self, weight=240, height=60):
        self.weight = weight
        self.height = height

    @staticmethod
    def rndcolor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    @staticmethod
    def rndcolor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def __call__(self):
        # 生成一张背景图片
        img = Image.new("RGB", [self.weight, self.height], "white")
        # 创建字体对象
        myfont = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', size=40)
        # 创建绘画对象
        draw = ImageDraw.Draw(img)
        # 随机填充背景图片的每个像素颜色
        for x in range(self.weight):
            for y in range(self.height):
                draw.point((x, y),fill=self.rndcolor())
        # 随机生成四个字母
        num = list()
        for i in range(4):
            word = random.choice(string.ascii_uppercase)
            num.append(word)
            #将随机生成的字母绘画到图片上
            draw.text((60*i +10, 10), str(word), font=myfont, fill=self.rndcolor2())
        print(num)
        img.save("code.jpg", "jpeg")
        # 模糊化处理
        img = img.filter(ImageFilter.BLUR)
        img.save("vcode.jpg", "jpeg")


if __name__ == '__main__':
    vcode = VCodeCreator()
    vcode()


