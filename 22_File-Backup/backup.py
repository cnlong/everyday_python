import os
import time
import wx


def backupfile(event):
    src_path = src_text.GetValue()
    target_dir = dest_text.GetValue()
    today_dir = target_dir + time.strftime('%Y%m%d')
    time_filename = time.strftime('%H%M%S')
    backup_filename = today_dir + os.sep +  time_filename + '.zip'
    command = 'zip -qr %s %s' % (backup_filename, src_path)
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)
    if os.system(command) == 0:
        print('Successful Backup')
    else:
        print('Failed Backup')


# 创建主程序App实例
app = wx.App()
# 创建顶层窗口
frame = wx.Frame(None, title='File Backup', pos=(1000, 200), size=(300, 150))
# 定义画布
panel = wx.Panel(frame)
# 定义组件，父级为panel
src_statictext = wx.StaticText(panel, label="源地址:")
src_text = wx.TextCtrl(panel)
dest_statictext = wx.StaticText(panel, label="目的地址:")
dest_text = wx.TextCtrl(panel)
backup_button = wx.Button(panel, label="备份")
# 绑定函数
backup_button.Bind(wx.EVT_BUTTON, backupfile)
# 创建第一个水平尺寸器
box = wx.BoxSizer()
# 添加第一栏到第一个水平尺寸器中
box.Add(src_statictext, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
box.Add(src_text, proportion=3, flag=wx.EXPAND|wx.ALL, border=3)
# 创建第二个水平尺寸器
box2 = wx.BoxSizer()
# 添加第二栏到第二个水平尺寸器中
box2.Add(dest_statictext, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
box2.Add(dest_text, proportion=3, flag=wx.EXPAND|wx.ALL, border=3)
# 添加一个垂直尺寸器
v_box = wx.BoxSizer(wx.VERTICAL)
# 将上述两个水平尺寸器和备份按钮添加到其中
v_box.Add(box, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
v_box.Add(box2, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
v_box.Add(backup_button, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)

# 设置主尺寸器
panel.SetSizer(v_box)

# 展示窗口
frame.Show()
# 开启程序
app.MainLoop()


