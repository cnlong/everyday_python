import os
import re


def stat_code(dir_path):
    if not os.path.isdir(dir_path):
        return
    exp_re = re.compile(r'^#.*')
    file_list = os.listdir(dir_path)
    print("%s\t%s\t%s\t%s" % ('file', 'all_lines', 'space_lines', 'exp_lines'))
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.py':
            with open(file_path, "r", encoding="UTF-8") as f:
                all_lines = 0
                space_lines = 0
                exp_lines = 0
                for line in f.readlines():
                    all_lines += 1
                    if line.strip() == '':
                        space_lines += 1
                        continue
                    exp = exp_re.findall(line.strip())
                    if exp:
                        exp_lines += 1
            print("%s\t%s\t%s\t%s" % (file, all_lines, space_lines, exp_lines))


if __name__ == '__main__':
    stat_code('code')