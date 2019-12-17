"""
按照上面的GUI代码有一个缺陷，由于我们各个组件都固定了大小，因此在框体拉伸时，对应的组件不会对应进行拉伸，比较影响用户体验。
通过尺寸器进行布局，类似于html中的css样式，通过尺寸器改写后，主窗口拉大或者缩小，中间的组件会随着窗口的大小比例尺寸进行改变
"""
import wx

def openfile(event):
    path = path_text.GetValue()
    with open(path, "r", encoding="utf-8") as f:
        content_text.SetValue(f.read())


app = wx.App()
frame = wx.Frame(None, title="Gui Test Editor", pos=(1000, 200), size=(500, 400))
# 定义一个画布面板，放置于frame中
panel = wx.Panel(frame)
# 定义panel中的组件
path_text = wx.TextCtrl(panel)
open_button= wx.Button(panel, label="打开")
open_button.Bind(wx.EVT_BUTTON, openfile)
save_button = wx.Button(panel, label="保存")
content_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

# 创建一个尺寸器实例,不带参数，默认为一个水平尺寸器，里面的组件水平排列
box = wx.BoxSizer()
# 将组件添加到尺寸器中，参数如下
# proportion：相对比例
# flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
# border：边框
box.Add(path_text, proportion=5, flag=wx.EXPAND|wx.ALL, border=3)
box.Add(open_button, proportion=2, flag=wx.EXPAND|wx.ALL, border=3)
box.Add(save_button, proportion=2, flag=wx.EXPAND|wx.ALL, border=3)

# wx.VERTICAL参数表示实例化一个垂直尺寸器,垂直排列组件
v_box = wx.BoxSizer(wx.VERTICAL)
# 将上述添加的水平尺寸器和另一个文本组件垂直排列
v_box.Add(box, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
v_box.Add(content_text, proportion=5, flag=wx.EXPAND|wx.ALL, border=3)

#设置主尺寸器
panel.SetSizer(v_box)

frame.Show()
app.MainLoop()