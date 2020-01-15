"""
分析nginx的访问日志，日志的输出是按照规则输出的
1.访问的客户端Ip
2.远程登录名称
3.认证的远程用户
4.请求的时间
5.UTC时间差
6.请求的HTTP方法
7.请求的资源
8.HTTP协议
9.HTTP状态码
10.服务端发送的字节数
11.访问来源
12.客户端浏览器信息
"""
from collections import Counter


# 用户访问ip的列表
ips = []
# 用户访问的资源
c = Counter()
# 统计返回状态码
d = dict()
with open("access.log") as f:
    for i in f:
        ips.append(i.split()[0])
        c[i.split()[6]] += 1
        key = i.split()[8]
        d.setdefault(key, 0)
        d[key] += 1
sum_requests = 0
error_requests = 0
for key, value in d.items():
    if int(key) >= 400:
        error_requests += value
    sum_requests += value

print('error rate: {0:.2f}'.format(error_requests*100/sum_requests))





print("PV is {0}".format(len(ips)))
# 集合去重
print("PV is {0}".format(len(set(ips))))
# 取访问次数最多的前十个
print("Popular resources: {0}".format(c.most_common(10)))