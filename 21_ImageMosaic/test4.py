import os
from PIL import Image
import argparse


def getImages(imageDir):
    """
    从小块图像目录中读取图像
    :param imageDir: 目录路径
    :return: 小块图像列表
    """
    files = os.listdir(imageDir)
    images = []
    for file in files:
        # os.path.join将目录名和文件名合成一个路径
        # os.path.abspath获取文件的绝对路径
        filePath = os.path.abspath(os.path.join(imageDir, file))
        with open(filePath, "rb") as f:
            im = Image.open(f)
            images.append(im)
            # 真实的图像数据直到试图处理该数据才会从文件读取（调用load()方法将强行加载图像数据）。
            im.load()
    return images


def getAverageRGB(image):
    """
    计算图像的RGB平均值
    每个像素点的RGB值分别累加除以像素点数量
    :param image: Image对象
    :return: 返回平均值
    """
    # 像素点数
    pixels = image.size[0] * image.size[1]
    Rlist = list()
    Glist = list()
    Blist = list()
    avg = list()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = image.getpixel((i, j))
            Rlist.append(r)
            Glist.append(g)
            Blist.append(b)
    # avg_r = sum(Rlist)/pixels
    # avg_g = sum(Glist)/pixels
    # avg_b = sum(Blist)/pixels
    # 每个像素点的r值总和除以像素点数
    avg.append(int(sum(Rlist)/pixels))
    avg.append(int(sum(Glist)/pixels))
    avg.append(int(sum(Blist)/pixels))
    return avg

    # npixels = image.size[0] * image.size[1]
    # cols = image.getcolors(npixels)
    # sumRGB = [(x[0] * x[1][0], x[0] * x[1][1], x[0] * x[1][2]) for x in cols]
    # avg = tuple([int(sum(x) / npixels) for x in zip(*sumRGB)])
    # return avg


def splitimage(image, size):
    """
    将图像按网格划分成多个小图像
    :param image: image对象
    :param size: 网格的列数和行数
    :return: 小图像列表
    """
    # 图片的宽和高
    W, H = image.size
    # 行数和列数，行数对比高度，列数对比宽度
    x, y = size
    # 获取每个小图像的宽度和高度
    w, h = int(W/y), int(H/x)
    imgs = []
    # 按照每行取出每列的小图像
    for j in range(x):
        for i in range(y):
            # crops裁剪图片，crop(左,上,右,下,)，"左,上"为小图像的左上点的坐标，"右,下"为小图像的右下点的坐标，
            imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return imgs


def getBestMatchIndex(input_avg, avgs):
    """
    寻找颜色值最近的一块小图像
    把颜色看做是三维空间中的一个点，依据目标点寻找列表中距离最近的一个点
    :param input_avg: 目标的颜色值
    :param avgs: 搜索的颜色值列表
    :return: 距离最近的颜色值图像的列表索引
    """
    # 初始索引为0
    # 列表自带索引，但是无法直接列出，索引设置默认索引，后续迭代，一直递增
    index = 0
    # 命中的索引
    min_index = 0
    # float("inf")表示正无穷，float("-inf")表示负无穷
    # 设置初始最小距离为正无穷
    min_dist = float("inf")
    # 遍历颜色值列表，索引从0开始
    for val in avgs:
        # 三维空间两点距离计算公式 (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        # + (z1 - z2) * (z1 - z2)，这里只需要比较大小，所以无需求平方根值
        dist = ((val[0] - input_avg[0]) * (val[0] - input_avg[0]) +
                (val[1] - input_avg[1]) * (val[1] - input_avg[1]) +
                (val[2] - input_avg[2]) * (val[2] - input_avg[2])
                )
        # 第一个计算出来的值肯定小于正无穷，将第一个计算出来的值设置为最小距离，最小距离的索引等于当前的索引值
        # 后续计算出来的值如果比第一个值小，就将新的值设置为最小值，并且最小距离的索引等于新值的索引值
        if dist < min_dist:
            min_dist = dist
            min_index = index
        # 索引递增
        index += 1
    # 遍历完颜色图标表中的所有元素，返回最小距离的颜色值元素索引
    return min_index


def createImageGrid(images, dims):
    """
    将图像列表里的小图像按先行后列的顺序填充到大图像中
    :param images: 小图像列表
    :param dims: 大图像的行数和列数
    :return: 返回拼接的新图像
    """
    # m为行数，对应高度，n为列数，对应宽度
    m, n = dims
    # 断言确保小图像的个数满足大图像切割后的网格数量
    assert m * n == len(images)
    # 计算出小图像中最大宽度和高度
    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])
    # 将计算出来的宽高作为每个网格宽高,创建新的大图像
    # 如果某个小图的宽高小于网格的宽高，剩余部分以背景色填充，默认是黑色
    grid_img = Image.new('RGB', (n * width, m * height))
    index = 0
    # # 依次按照先行后列的顺序，依次将小图像填充过去
    for i in range(m):
        for j in range(n):
            # paste(img, (左上角x坐标，左上角y坐标))
            # print(i, j)
            grid_img.paste(images[index], (j * height, i * width))
            # 索引递增，一张图片一张图片的填充
            index += 1
    # 依次将每个小图像粘贴到大图像里
    # for index in range(len(images)):
    #     # 计算要粘贴到网格的哪行
    #     row = int(index / n)
    #     # 计算要粘贴到网格的哪列
    #     col = index - n * row
    #     # 根据行列数以及网格的大小得到网格的左上角坐标，把小图像粘贴到这里
    #     grid_img.paste(images[index], (col * width, row * height))
    return grid_img


def createPhotomosaic(target_image, grid_size, input_imageDir):
    """生成图片马赛克主函数"""
    # 切割目标图像为网格小图像
    print(">>>目标图片切割")
    with open(target_image, "rb") as f:
        content = Image.open(f)
        target_images = splitimage(content, grid_size)
    print(">>>读取备选图片列表")
    # 读取图像列表
    input_images = getImages(input_imageDir)
    print(">>>备选图片列表颜色平均值")
    # 计算图像列表中所有图像的颜色平均值
    avgs = list()
    for img in input_images:
        avgs.append(getAverageRGB(img))
    print(">>>获取替换图片列表")
    # 匹配到的图像列表的中的小图像新组成一个列表
    output_images = list()
    # 计算目标图像被切割的每个网格小图像的颜色平均值
    for img in target_images:
        avg = getAverageRGB(img)
        # 并和图像列表中的颜色平均值对比，找到合适的图像的索引
        match_index = getBestMatchIndex(avg, avgs)
        output_images.append(input_images[match_index])
    print(">>>生成新图像")
    # 将新生成的替换图片列表填充到新生成的图像中
    mosaic_image = createImageGrid(output_images, grid_size)
    return mosaic_image


def main():
    """主函数，接收命令行动态传参"""
    # 定义命令行对象
    parser = argparse.ArgumentParser(description="Create a photomosaic from input images")
    # 添加参数
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile')
    # 解析命令行参数
    args = parser.parse_args()
    grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))
    output_filename = 'mosaic.png'
    if args.outfile:
        output_filename = args.outfile
    target_image = args.target_image
    input_imageDir = args.input_folder
    mosaic_image = createPhotomosaic(target_image, grid_size, input_imageDir)
    mosaic_image.save(output_filename, 'PNG')
    print("Success!")


if __name__ == '__main__':
    main()