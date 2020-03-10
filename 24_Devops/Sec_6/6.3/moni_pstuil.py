import os
import socket
from datetime import datetime
import jinja2
import yagmail
import psutil


# 邮件发送的相关地址信息
# 注意这里的账户必须是smtp的账户，不是普通账户密码
EMAIL_USER = 'l17625924672@163.com'
EMAIL_PASSWORD = 'chenchen6666'
RECIPIENTS = ['271138425@qq.com']


def bytes2human(n):
    """
    单位转换
    :param n: 需要转换的
    :return:
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = dict()
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def get_cpu_info():
    """
    获取CPU的相关信息
    :return: 字典形式返回CPU的相关信息
    """
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    return dict(cpu_count=cpu_count, cpu_percent=cpu_percent)


def get_memory_info():
    """
    获取内存信息
    :return: 字典形式返回
    """
    virtual_mem = psutil.virtual_memory()
    mem_total = bytes2human(virtual_mem.total)
    mem_percent = virtual_mem.percent
    mem_free = bytes2human(virtual_mem.free + virtual_mem.buffers + virtual_mem.cached)
    mem_used = bytes2human(virtual_mem.total * virtual_mem.percent)

    return dict(mem_total=mem_total, mem_percent=mem_percent,
                mem_free=mem_free, mem_used=mem_used)


def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_total = bytes2human(disk_usage.total)
    disk_percent = disk_usage.percent
    disk_free = bytes2human(disk_usage.free)
    disk_used = bytes2human(disk_usage.used)

    return dict(disk_total=disk_total, disk_percent=disk_percent,
                disk_free=disk_free, disk_used=disk_used)


def get_boot_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    return dict(boot_time=boot_time)


def collect_monitor_data():
    """
    将所有收集到的信息统一添加到一个字典中
    :return: 所有数据构成的字典
    """
    data = dict()
    data.update(get_boot_info())
    data.update(get_cpu_info())
    data.update(get_disk_info())
    data.update(get_memory_info())
    return data


def render(tpl_path, **kwargs):
    """
    使用Jinja2根据传参进行渲染，渲染之后得到一个HTML形式的字符串
    :param tpl_path:
    :param kwargs:
    :return:
    """
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path)).get_template(filename).render(**kwargs)


def main():
    # 获取主机名
    hostname = socket.gethostname()
    data = collect_monitor_data()
    data.update(dict(hostname=hostname))
    # 获取渲染的HTML文件
    content = render("monitor.html", **data)
    print(content)
    # 发送邮件，注意这里的端口
    with yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD,
                      host='smtp.163.com', port=587) as yag:
        for recipient in RECIPIENTS:
            yag.send(recipient, "监控信息", content)


if __name__ == '__main__':
    main()