import json
import argparse
from collections import defaultdict
from contextlib import contextmanager
import pymysql


def parse_args():
    """
    定义函数获取命令行参数
    :return:
    """
    parser = argparse.ArgumentParser(description="Get Inventory")
    # 添加互斥组，组内加入两个参数，同时出现的时候会报错
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true', help='List active servers')
    group.add_argument('--host', help='List details about the specific host')
    return parser.parse_args()


# 使用contextmanager装饰一个生成器，使其成为一个上下文管理器，无需__enter__和__exit__
@contextmanager
def get_conn(**kwargs):
    """
    连接数据库
    :param kwargs: 数据库连接参数
    :return:
    """
    conn = pymysql.connect(**kwargs)
    try:
        yield conn
    finally:
        conn.close()


# 从数据库中获取所有主机
def list_all_hosts(conn):
    # 定义默认字典类型,defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值。
    hosts = defaultdict(list)

    # 打开一个数据库连接
    with conn as cur:
        # 查看hosts数据库
        cur.execute('select * from hosts')
        rows = cur.fetchall()
        for row in rows:
            id, host, group, user, port = row
            # 将主机加入对应的主机组列表中
            hosts[group].append(host)
        return hosts


# 查询指定的主机信息
def get_host_detail(conn, host):
    details = {}
    with conn as cur:
        cur.execute("select * from hosts where host='{0}'".format(host))
        rows = cur.fetchall()
        if rows:
            id, host, group, user, port = rows[0]
            details.update(ansible_user=user, ansible_port=port)
        return details


# 将字典json格式输出
def to_json(in_dict):
    return json.dump(in_dict, sort_keys=True, indent=2)


def main():
    parser = parse_args()
    # 打开数据库
    with get_conn(host='127.0.0.1', user='root', password='123456', db='test') as coon:
        # 如果传入list参数
        if parser.list:
            # 获取所有主机
            hosts = list_all_hosts(coon)
            # json格式输出
            print(to_json(hosts))
        else:
            # 如果传入host参数
            # 单独打印某个主机的信息
            details = get_host_detail(coon, parser.host)
            print(to_json(details))


if __name__ == '__main__':
    main()