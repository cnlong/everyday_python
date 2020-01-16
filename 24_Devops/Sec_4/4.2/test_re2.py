import re
import time


def main():
    pattern = "[0-9]+"
    re_obj = re.compile(pattern)
    with open("data.txt") as f:
        for line in f:
            re_obj.findall(line)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("执行时间：%s" % (time.time() - start_time))