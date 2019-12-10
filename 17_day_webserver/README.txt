使用 Python 语言实现一个 Web 服务器，探索 HTTP 协议和 Web 服务的基本原理，同时学习 Python 如何实现 Web 服务请求、响应、错误处理及CGI协议，最后会根据项目需求使用 Python 面向对象思路对代码进行重构。
BaseHTTPServer库有两个类HTTPServer和BaseHTTPRequestHandler
HTTPServer:
    继承SocketServer.TCPServer，用于获取请求，并将请求分配给应答程序处理
    无需手动创建socket就可以实现套接字监听端口，实现web服务器，较为方便，但是此模块不作为生产服务器使用，因为其不够完善，只能做简单服务器使用

BaseHTTPRequestHandler:
    继承SocketServer.StreamRequestHandler，对http连接的请求作出应答（response）

