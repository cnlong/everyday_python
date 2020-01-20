with open('/tmp/data.txt', 'w') as f:
    print(1, 2, 'hello, world!', sep=',', file=f)


with open('/tmp/data.txt') as f:
    for line in f:
        print(line.upper())