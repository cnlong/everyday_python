import re
import time


def main():
    pattern = "[0-9]+"
    with open("data.txt") as f:
        for line in f:
            re.findall(pattern, line)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("执行时间：%s" % (time.time() - start_time))