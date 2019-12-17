import wx


# 创建一个App实例
app = wx.App()
# 创建一个顶层窗口，wx.Frame(Parent, Id, Title)，（一个父窗口名，后面紧随着它的Id, 标题）,使用None,表示没有父窗口
frame = wx.Frame(None)
# 窗口展示，默认为True.如果为False，窗口不可见
frame.Show(True)
# 开启程序，处理事件
app.MainLoop()