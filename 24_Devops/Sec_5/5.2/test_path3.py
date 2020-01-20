import os
import sys


def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + 'dose not exists')
    elif not os.access(filename, os.R_OK):
        os.chmod(filename, 777)
    else:
        with open(filename) as f:
            print(f.read())


if __name__ == '__main__':
    main()