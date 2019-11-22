from PIL import Image

im = Image.open("cat.jpg", "r")
print(im)
print(im.size, im.format, im.mode)
# im.show()
# im.save("cat.png")
# im = Image.open("cat.png", "r")
# print(im)
# print(im.size, im.format, im.mode)

im.resize((238,98), resample=Image.BICUBIC)
im.save("new.png")