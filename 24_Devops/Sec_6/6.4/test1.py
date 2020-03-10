import pyinotify

# 创建一个监视对象
vm = pyinotify.WatchManager()

# 向监视对象中添加对文件的监视事件,pyinotify.ALL_EVENTS表示所有的事件
vm.add_watch('/tmp', pyinotify.ALL_EVENTS)

# 或者可以指定需要监控的事件，例如仅监控创建和删除事件
# mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE
# vm.add_watch('/tmp', mask)

# 通过Notifier根据watchmanager中的配置确定需要处理的事件
notifier = pyinotify.Notifier(vm)

# 循环处理事件，最后的结果和python -m pyinotify /tmp 的效果一样，阻塞状态，有检测信息才会解阻塞
notifier.loop()