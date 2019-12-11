"""
1.重写do_GET方法的时候，多个条件的时候，需要做多个判断，后续更改，需要对源代码继续修改，容易出错
2.功能扩展的时候尽量不修改源代码
3.将此前的代码进行修改更新，对多个条件进行封装，然后调用，这样更为稳妥
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class ServerException(Exception):
    """自定义服务器内部错误类"""
    pass


class CaseNoFile(object):
    """定义请求的文件不存在情况下的处理类"""
    # 传入请求处理实例作为实参，通过full_path获取其实例属性，判断其存在与否
    def test(self, requesthandler):
        # os.path.exists判断文件存在与否，不存在为False,存在即为True
        return not os.path.exists(requesthandler.full_path)

    # 定义此类的处理方法
    def act(self, requesthandler):
        requesthandler.handle_error(ServerException("'{0}' not found".format(requesthandler.path)))
        raise ServerException("'{0}' not found".format(requesthandler.path))


class CaseExFile(object):
    """定义请求的文件存在且为文件的情况下的处理类"""
    # 判断请求的文件是否为文件，是为True
    def test(self, requesthandler):
        return os.path.isfile(requesthandler.full_path)

    def act(self, requesthandler):
        requesthandler.handle_file(requesthandler.full_path)


class CaseIndex(object):
    """定义默认页面处理情况"""
    # 组合index_path的请求路径
    def index_path(self, requesthandler):
        return os.path.join(requesthandler.full_path, 'index.html')

    # 判断原请求是否是个目录，默认不加URL的请求是根目录
    def test(self, requesthandler):
        return os.path.isdir(requesthandler.full_path) and os.path.isfile(self.index_path(requesthandler))

    # 返回默认文件
    def act(self, requesthandler):
        return requesthandler.handle_file(self.index_path(requesthandler))


class CaseExDir(object):
    """定义请求的文件存在且为目录的情况下的处理类"""
    def test(self, requesthandler):
        return os.path.isdir(requesthandler.full_path)

    def act(self, requesthandler):
        requesthandler.handle_error(ServerException("Unknown object '{0}'".format(requesthandler.path)))
        raise ServerException("Unknown object '{0}'".format(requesthandler.path))


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
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    # 定义所有可能出现的情况，便于后续遍历
    Cases = [CaseNoFile(), CaseExFile(), CaseIndex(), CaseExDir()]

    def do_GET(self):
        # 定义新属性请求文件的完整路径
        self.full_path = os.getcwd() + self.path
        # 遍历所有出现的情况
        for case in self.Cases:
            # 将请求实例RequestHandler作为实参带入到情况类的方法中进行判断
            # 为True则继续
            if case.test(self):
                # 对应调用其act方法
                case.act(self)
                # 调用完成终止此循环
                break

    # win平台下，open函数会默认以gbk编码打开文件，需要指定编码
    def handle_file(self, full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.send_content(content)

    # 定义错误处理函数，对错误网页页面进行格式化处理
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content)

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
