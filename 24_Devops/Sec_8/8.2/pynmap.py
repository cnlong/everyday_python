import nmap


# 创建一个PortSanner对象
nm = nmap.PortScanner()

# 调用对象的scan方法完成基本的端口扫描
nm.scan('192.168.6.31,32', '22,8080')

# 命令行参数
print(nm.command_line())

# 扫描方法
print(nm.scaninfo())

# 主机列表
print(nm.all_hosts())

# 获取单台主机的网络状态
print(nm['192.168.6.31'].state())

# 获取单台主机的所有协议
print(nm['192.168.6.31'].all_protocols())

# 获取单台主机的所有打开的端口号
print(nm['192.168.6.31']['tcp'].keys())

# 获取单台主机的端口号对应的服务
print(nm['192.168.6.31']['tcp'][8080])

print(nm.scan(hosts='192.168.6.0/30', arguments='-n -sP -PE -PA21,23,80,3389'))