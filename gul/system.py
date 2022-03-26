import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import ttk  # 导入内部包
# 定义列的名称
root = tk.Tk()
root.title("基于海岸水文学数据处理多用途集成工具系统")
root.geometry("800x600")
paneroot = ttk.Panedwindow(root, orient=tk.HORIZONTAL)  # 添加水平方向的推拉窗组件
paneroot.grid(row=0, column=0, sticky=tk.NSEW)  # 向四个方向拉伸填满Mrootdow帧

frmleft = ttk.Frame(paneroot, relief=tk.SUNKEN, padding=0)  # 左侧Frame帧用于放置播放列表


frmRight = ttk.Frame(paneroot, relief=tk.SUNKEN)  # 右侧Frame帧用于放置视频区域和控制按钮
frmRight.grid(row=0, column=0, sticky=tk.NSEW)  # 右侧Frame帧四个方向拉伸
frmRight.rowconfigure(0,weight=1)
frmRight.columnconfigure(0,weight=1)

paneroot.add(frmRight, weight=1)  # 将左侧Frame帧添加到推拉窗控件，左侧权重1

tabControl = ttk.Notebook(frmRight)  #创建Notebook
tab1 = tk.Frame(tabControl,bg = "blue")  #增加新选项卡
tabControl.add(tab1, text='衍生要素计算(S、d、D、V)')  #把新选项卡增加到Notebook
tab2 = tk.Frame(tabControl,bg='yellow')
tabControl.add(tab2, text='飓风浪相关参数的计算')
tab3 = tk.Frame(tabControl)
tabControl.add(tab3, text='各种累积频率波高间的换算')
#--------------------------------------------------
menubar = tk.Menu(root)
fileMenu = tk.Menu(menubar, tearoff=0)  # 去掉顶端横线
menubar.add_cascade(label='文件', menu=fileMenu)  # 添加一个子菜单 File
fileMenu.add_command(label='新建' )
fileMenu.add_command(label='打开')
fileMenu.add_command(label='保存', accelerator="Ctrl+S")
fileMenu.add_command(label='另存为')
fileMenu.add_separator()  # 加分割线
fileMenu.add_command(label='退出', command=quit)
editMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editMenu)
editMenu.add_command(label='剪切')
editMenu.add_command(label='复制')
editMenu.add_command(label='粘贴')
settingsMenu = tk.Menu(editMenu, tearoff=0)
editMenu.add_cascade(label='设置', menu=settingsMenu)
root.config(menu=menubar)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.mainloop()