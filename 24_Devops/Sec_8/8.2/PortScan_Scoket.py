from socket import *


def port_scan(host, port):
    """
    端口扫描函数
    :param host: 主机地址
    :param port: 主机端口
    :return: 无返回
    """
    # 建立socket对象。默认是网络通信和TCP协议
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        # 连接主机端口,尝试建立连接，成功打印消息，失败报错
        conn.connect((host, port))
        print("%s:%s is avaliable" % (host, port))
    except Exception as err:
        print(("%s:%s is not avaliable" % (host, port)))
    finally:
        # 关闭连接
        conn.close()


def main():
    host = '192.168.6.31'
    for port in range(20, 5000):
        port_scan(host, port)


if __name__ == '__main__':
    main()