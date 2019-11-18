from PIL import Image,ImageDraw

blank = Image.new("RGB", [1024,768], "white")
drawblk = ImageDraw.Draw(blank)
drawblk.line([100, 100, 100, 600], fill='red')
drawblk.line([100, 100, 600, 100], fill='red')
drawblk.line([100, 600, 600, 600], 'black')
drawblk.line([600, 100, 600, 600], 'red')
drawblk.arc([100, 100, 600, 600], 0, 360, 'red')
drawblk.arc([200, 100, 500, 600], 0, 360, 'red')

blank.save('white.jpg', 'jpeg')
# im = Image.open('white.jpg', 'r')
# im.show()

text = 'i\'m very happy'

drawblk.ink = 0 + 0 * 256 + 255 * 256 * 256
drawblk.text([300, 500],text)
blank.save('back.jpg', 'jpeg')
im2 = Image.open('back.jpg', 'r')
im2.show()