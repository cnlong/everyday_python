"""
mysql压测小工具
通过多线程的多数据插入，向专门用于测试的数据库表中插入数据，验证其性能
"""
import argparse
from contextlib import contextmanager
import pymysql
import string
import random
import time
import threading

# 定义用于压测的数据库及表格
DB_NAME = "test_insert_data_db"
TABLE_NAME = "test_insert_data_table"
CREATE_TABLE_STATEMENT = """create table {0} (id int(10) NOT NULL AUTO_INCREMENT,
                            name varchar(255) NOT NULL ,
                            datetime double NOT NULL ,
                            primary key (id));""".format(TABLE_NAME)


# 1.从命令行获取参数
def _argparse():
    """私有函数，内部调用，获取命令行参数"""
    # 创建参数对象
    parser = argparse.ArgumentParser(description='benchmark tool for MySQL database')
    # 添加命令参数
    # action='store',默认action模式，存储值到指定变量中
    parser.add_argument('--host', action='store', dest='host', required=True, help='connect to host')
    parser.add_argument('--user', action='store', dest='user', required=True, help='user for login')
    parser.add_argument('--password', action='store', dest='password', required=True, help='password to use when connecting to server')
    parser.add_argument('--port', action='store', dest='port', default=3306, type=int, help='port to use for connection')
    parser.add_argument('--thread_size', action='store', dest='thread_size', default=5, type=int, help='how much connection for db')
    parser.add_argument('--row_size', action='store', dest='row_size', default=5000, type=int, help='how much rows')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    # 返回一个NameSpace对象,用于解析命令行参数，获取对象后，参数值可以通过属性的方式进行访问
    return parser.parse_args()


# 2.连接数据库，使用生成器和装饰器，自定义上下文管理器
@contextmanager
def get_conn(**kwargs):
    conn = pymysql.connect(**kwargs)
    try:
        yield conn
    finally:
        conn.close()


# 3.新建连接，删除旧的用于测试的数据库，并新建用于测试的数据库
def create_db_and_table(conn):
    with conn as cur:
        for sql in ["drop database if exists {0}".format(DB_NAME),
                    "create database {0}".format(DB_NAME),
                    "use {0}".format(DB_NAME),
                    CREATE_TABLE_STATEMENT]:
            try:
                print("start execute {0}".format(sql))
                cur.execute(sql)
                print("{0} execute successfully!")
            except Exception as e:
                print(e)


# 4.随机获取字符串
def random_string(length=10):
    # 获取所有的字母和数字，组成一个字符串
    s = string.ascii_letters + string.digits
    # 从上述字符串中随机获取一组长度为10的列表，并组合成字符串
    return "".join(random.sample(s, length))


# 5.随机生产的sql数据插入
def add_row(cursor):
    # 注意sql语言的规范，字符串需要加引号
    SQL_FORMAT = """INSERT INTO {0} (name, datetime) values ('{1}', {2}) """
    sql = SQL_FORMAT.format(TABLE_NAME, random_string(), time.time())
    cursor.execute(sql)


# 6.向数据库中插入数据
def insert_data(conn_args, row_size):
    with get_conn(**conn_args) as conn:
        with conn as c:
            c.execute('use {0}'.format(DB_NAME))
        with conn as c:
            for i in range(row_size):
                # 插入数据
                add_row(c)
                # 提交事务
                conn.commit()


def main():
    # 获取命令行参数解释对象
    parser = _argparse()
    # 获取数据库传参，并组成字典
    conn_args = dict(host=parser.host, user=parser.user,
                     password=parser.password, port=parser.port)
    # 连接数据库，创建用于测试的数据库及表
    with get_conn(**conn_args) as conn:
        create_db_and_table(conn)

    # 线程列表
    threads = []
    # 根据线程数遍历创造线程插入数据
    for i in range(parser.thread_size):
        # 创建线程
        t = threading.Thread(target=insert_data, args=(conn_args, parser.row_size))
        threads.append(t)
        t.start()

    # 阻塞主进程，等待线程执行完成
    for t in threads:
        t.join()


if __name__ == '__main__':
    t = time.time()
    main()
    print("耗时：{0}".format(time.time() - t))
