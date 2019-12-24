from PIL import Image
import re


try:
    img = Image.open("oxygen.png")
    data = [img.getpixel((i, j)) for i in range(0, 609) for j in range(43, 53)]
    row = [chr(img.getpixel((i, 45))[0]) for i in range(0, 609, 7)]
    # print(len(row))
    content = "".join(row)
    print(content)
    a = re.findall(r"\d+", content)
    content = [chr(int(i)) for i in a]
    print("".join(content))
except Exception as e:
    print(e)