with open('testfile.txt') as f:
    while True:
        chunk = f.read(10)
        if not chunk:
            break
        else:

            print(chunk)