import pyinotify

vm = pyinotify.WatchManager()
# 定制事件类别
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Creating:", event.pathname)

    def process_IN_DELETE(self, event):
        print("Removing", event.pathname)


# 对象实例
handler = EventHandler()
vm.add_watch('/tmp', mask, rec=True)
# 通过notifier根据vm的配置及处理方式来处理事件
notifier = pyinotify.Notifier(vm, handler)
notifier.loop()

