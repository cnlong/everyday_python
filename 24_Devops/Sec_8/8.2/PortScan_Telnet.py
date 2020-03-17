import telnetlib


def port_scan(host, port):
    # 建立一个telnet对象
    t = telnetlib.Telnet()
    try:
        # 尝试连接
        t.open(host, port, timeout=1)
        print("%s:%s is avaliable" % (host, port))
    except Exception as err:
        print(("%s:%s is not avaliable" % (host, port)))
    finally:
        # 关闭连接
        t.close()


def main():
    host = '192.168.6.31'
    for port in range(20, 100):
        port_scan(host, port)


if __name__ == '__main__':
    main()