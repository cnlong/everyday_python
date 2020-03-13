import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS


def get_image_meta_info(filename):
    exif_data = dict()
    with Image.open(filename) as img:
        # 先获取编码与数值的字典
        data = img._getexif()
        for tag, value in data.items():
            # 解码获取新数据，并存入到字典中
            decoded = TAGS.get(tag)
            exif_data[decoded] = value

        # GPS信息的转换,GPS的信息会以字典的形式作为值存储
        if exif_data['GPSInfo']:
            gps_data = dict()
            for tag, value in exif_data['GPSInfo'].items():
                decoded = GPSTAGS.get(tag)
                gps_data[decoded] = value
            exif_data['GPSInfo'] = gps_data

    return exif_data


def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.exists(filename):
        return SystemExit("{0} is not exists".format(filename))
    exif_data = get_image_meta_info(filename)
    for key, value in exif_data.items():
        # sep定义输出数据之间的间隔
        print(key, value, sep=":")


if __name__ == '__main__':
    main()