import wx


app = wx.App()
frame = wx.Frame(None, title="Gui Test Editor", pos=(1000, 200), size=(500, 400))
# 定义文本框组件
path_text = wx.TextCtrl(frame, pos=(5, 5), size=(350, 24))
# style=wx.TE_MULTILINE 实现文本自动换行
content_text = wx.TextCtrl(frame, pos=(5, 39), size=(475, 300), style=wx.TE_MULTILINE)
# 定义打开按钮组件
open_button = wx.Button(frame, label="打开", pos=(370, 5), size=(50,24))
# 定义保存按钮组件
save_button = wx.Button(frame, label="保存", pos=(430, 5), size=(50,24))


# 定义打开文件的事件函数
def openfile(event):
    # 获取path_text组件中写入的值，也就是文件名
    path = path_text.GetValue()
    with open(path, "r", encoding="utf-8") as f:
        # 将打开的文件内容保存到content_text组件中
        content_text.SetValue(f.read())


# 将打开文件的事件绑定到打开按钮组件上
open_button.Bind(wx.EVT_BUTTON, openfile)

frame.Show()
app.MainLoop()