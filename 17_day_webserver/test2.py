
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class ServerException(Exception):
    """定义服务器内部错误类"""
    pass


class RequestHandler(BaseHTTPRequestHandler):
    """定义类用于处理请求"""
    # 定义页面模板
    Page = """\
        <html>
        <body>
        <table>
            <tr>  <td>Header</td>         <td>Value</td>          </tr>
            <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
            <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
            <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
            <tr>  <td>Command</td>        <td>{command}</td>      </tr>
            <tr>  <td>Path</td>           <td>{path}</td>         </tr>
        </table>
        </body>
        </html>
    """

    def do_GET(self):
        # os.getcwd()列出当前程序所在的完整路径，和访问请求的路径组合成完整路径
        full_path = os.getcwd() + self.path
        # 判断请求的路径是否存在
        if os.path.exists(full_path):
            # 判断请求的URL是文件
            if os.path.isfile(full_path):
                content = self.handle_file(full_path)
                self.send_content(content)
            # 如果不是文件，是目录则报错
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))
        else:
            raise ServerException("'{0}' not found".format(self.path))

    def handle_file(self,full_path):
        with open(full_path, "r") as f:
            content = f.read()
        return content

    # 封装HTML页面创建函数
    def create_page(self):
        # 通过基类自带的方法获取相关属性的值，并格式化输出到网页模板中
        vlaues = {
            'date_time':   self.date_time_string(),  # 获取时间戳
            'client_host': self.client_address[0],   # 获取客户端地址
            'client_port': self.client_address[1],   # 获取客户端端口，通常和地址组成一个元组
            'command':     self.command,  # 获取请求类型，例如GET、POST
            'path':        self.path  # 获取请求路径，例如/index.html
        }
        # 将上述的字典逐一格式化输出的此前定义的web模板中
        page = self.Page.format(**vlaues)
        # 返回新的网页
        return page

    # 封装回复数据函数
    def send_content(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
