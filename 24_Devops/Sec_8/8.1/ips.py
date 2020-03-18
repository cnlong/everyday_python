with open('ips.txt', 'w') as f:
    for i in range(1,255):
        f.write("192.168.6." + str(i) + '\n')