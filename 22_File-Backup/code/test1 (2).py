from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random


back = Image.new("RGB", [140, 50], "gray")
back.save("vcode.jpg")
im = Image.open("vcode.jpg")
myfont = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', size=40)
draw = ImageDraw.Draw(im)
num = list()
for i in range(4):
    word = random.choice(string.ascii_uppercase)
    num.append(word)
# print(num)
draw.text((10,5), str(num[0]), font=myfont, fill="red")
draw.text((40,5), str(num[1]), font=myfont, fill="red")
draw.text((70,5), str(num[2]), font=myfont, fill="red")
draw.text((100,5), str(num[3]), font=myfont, fill="red")
vcode = im.filter(ImageFilter.BLUR)

vcode.show()