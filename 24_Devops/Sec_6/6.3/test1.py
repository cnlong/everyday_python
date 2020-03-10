import psutil

print("逻辑CPU个数：" + str(psutil.cpu_count()))
print("物理CPU个数：" + str(psutil.cpu_count(logical=False)))

print("到目前为止总的CPU利用率：" + str(psutil.cpu_percent()))
print("到目前为止每个CPU利用率：" + str(psutil.cpu_percent(percpu=True)))
print("两秒内每个CPU利用率：" + str(psutil.cpu_percent(interval=2, percpu=True)))

print("CPU时间：" + str(psutil.cpu_times()))

print("CPU耗费时间占比：" + str(psutil.cpu_times_percent()))

print("CPU的统计信息：" + str(psutil.cpu_stats()))

print("内存的使用情况：" + str(psutil.virtual_memory()))

print("交换分区的使用情况：" + str(psutil.swap_memory()))

print(psutil.disk_partitions())

print(psutil.disk_usage('/'))

print(psutil.disk_io_counters())

print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))
print(psutil.net_connections())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())

print(psutil.users())

print(psutil.boot_time())
