"""
http server module
This module defines classes for implementing HTTP servers (Web servers).
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

# BaseHTTPRequestHandler是这个模块中用于处理程序请求的，通常用此类作为基类，重写方法，创建自己特殊处理的方法
class RequestHandler(BaseHTTPRequestHandler):
    """定义类用于处理请求"""
    # 定义请求回复的body部分
    page = """\
        <html>
        <body>
        <p>hahaha</p>
        </body>
        </html>
    """

    # 重写do_Get,处理get请求,类似的可以重写其他do_*方法
    def do_GET(self):
        # 设置回复的状态码
        self.send_response(200)
        # 设置回复的头部信息
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.page)))
        # 发送空白行，标识头部信息结束，便于body和header分开
        self.end_headers()
        # 应答的HTTP文本流对象，输出流回写html源码数据
        self.wfile.write(self.page.encode("utf-8"))

if __name__ == '__main__':
    # 定义服务器地址和端口
    serverAddress = ('', 8080)
    # 创建一个server类，传入服务器信息参数和处理请求的类
    server = HTTPServer(serverAddress, RequestHandler)
    # 运行服务器终端程序
    server.serve_forever()
