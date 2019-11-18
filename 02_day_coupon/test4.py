with open("coupondata.txt", "r") as f:
    # for i in f.readlines():
    #     print(i)
    #     print("="*50)
    while True:
        text = f.readline()
        if not text:
            break
        print(text, end="")