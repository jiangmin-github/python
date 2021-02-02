# coding:utf-8

"This is my first python program to calculate the vectors"

import tkinter as tk
import tkinter.messagebox as mb
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mpl_toolkits.axisartist as axt
import matplotlib.pyplot as plt
import numpy as np

def ShowVector(x1,y1,x2,y2,x3,y3,which_button):

    #创建画布
    fig = plt.figure()

    #使用axisartist.Subplot方法创建一个绘图区对象ax
    ax = axt.Subplot(fig, 111)

    #将绘图区对象添加到画布中
    fig.add_axes(ax)
    
    # 通过set_visible方法设置绘图区所有坐标轴隐藏
    ax.axis[:].set_visible(False)

    # ax.new_floating_axis代表添加新的坐标轴
    ax.axis["x"] = ax.new_floating_axis(0,0)

    # 给x坐标轴加上箭头
    ax.axis["x"].set_axisline_style("->", size = 1.5)

    # 添加y坐标轴，且加上箭头
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.5)

    # 设置x、y轴上刻度显示方向
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")

    xmax = np.max([abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3)])
    ax.set_xlim(-xmax-0.5,xmax+0.5)
    ax.set_ylim(-xmax-0.5,xmax+0.5)

    slb5.set('(' + str("%3.4f" % x3) + ' , ' + str("%3.4f" % y3) + ')')
  
    # draw the lines
    ax.arrow(0, 0, x1, y1,
             length_includes_head=True,# 增加的长度包含箭头部分
             head_width=0.2, head_length=0.3, fc='r', ec='r')
    ax.grid()

    ax.arrow(0, 0, x2, y2,
             length_includes_head=True,# 增加的长度包含箭头部分
             head_width=0.2, head_length=0.3, fc='b', ec='b')
    ax.grid()

    ax.arrow(0, 0, x3, y3,
             length_includes_head=True,# 增加的长度包含箭头部分
             head_width=0.2, head_length=0.3, fc='y', ec='y')
    ax.grid()

    if which_button == "Plus":
        plt.plot([x1,x3] , [y1,y3] , c = 'grey')
        plt.plot([x2,x3] , [y2,y3] , c = 'grey')

    if which_button == "Minus":
        plt.plot([x2,x1] , [y2,y1] , c = 'grey')
        plt.plot([x3,x1] , [y3,y1] , c = 'grey')

    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5,column=1,rowspan=1,columnspan=4)

def GetVectorResult(which_button):
    s1 = ""
    
    try:
        x1 = float(v1x.get())
        y1 = float(v1y.get())
        x2 = float(v2x.get())
        y2 = float(v2y.get())
    except:
        s1 = "Invalid float input"

    if s1 == "":
        if which_button == "Plus":
            x3 = x1 + x2
            y3 = y1 + y2
            ShowVector(x1,y1,x2,y2,x3,y3,"Plus")
        elif which_button == "Minus":
            x3 = x1 - x2
            y3 = y1 - y2
            ShowVector(x1,y1,x2,y2,x3,y3,"Minus")
        elif which_button == "Inner":
    	    s1 = str("%3.4f" % (x1 * x2)) + ' , ' + str("%3.4f" % (y1 * y2))
        elif which_button == "Outer":
    	    s1 = str("%3.4f" % (x1 / x2)) + ' , ' + str("%3.4f" % (y1 / y2))
    else:
        mb.showinfo(title = which_button, message = s1)

# define the Button process function
def ProcessButtonPlus():
	GetVectorResult("Plus")

# define the Button process function
def ProcessButtonMinus():
	GetVectorResult("Minus")

# define the Button process function
def ProcessButtonInner():
	GetVectorResult("Inner")

# define the Button process function
def ProcessButtonOuter():
	GetVectorResult("Outer")

# define the Button process function
def ProcessButtonQuit():
    top.quit()
    top.destroy()

top = tk.Tk()  #创建顶层窗口

top.geometry('850x650')  #初始化窗口大小
top.title("VectorCalc") 

slb5 = tk.StringVar()

# Creatr Labels
lb1 = tk.Label(top,text='X').grid(row=1,column=2)
lb2 = tk.Label(top,text='Y').grid(row=1,column=3)
lb3 = tk.Label(top,text='Enter Vecter1: ').grid(row=2,column=1)
lb4 = tk.Label(top,text="Enter Vecter2: ").grid(row=3,column=1) 
lb4 = tk.Label(top,text="The Result is : ").grid(row=4,column=1)
lb5 = tk.Label(top,textvariable=slb5).grid(row=4,column=2,rowspan=1,columnspan=2)  

v1x = tk.StringVar()
v1y = tk.StringVar()
v2x = tk.StringVar()
v2y = tk.StringVar()

# Create Vector1 Entry
ev1x = tk.Entry(top,textvariable=v1x,width=30,justify="center")
ev1x.grid(row=2,column=2)  
ev1y = tk.Entry(top,textvariable=v1y,width=30,justify="center")
ev1y.grid(row=2,column=3) 

# Create Vector2 Entry
ev2x = tk.Entry(top,textvariable = v2x,width=30,justify="center")
ev2x.grid(row = 3,column = 2)  
ev2y = tk.Entry(top,textvariable = v2y,width=30,justify="center")
ev2y.grid(row = 3,column = 3) 

# 创建按钮，点击按钮时触发processButton函数
bt1 = tk.Button(top,text="Plus",command=ProcessButtonPlus).grid(row=2,column=5)
bt2 = tk.Button(top,text="Minus",command=ProcessButtonMinus).grid(row=2,column=6)
bt3 = tk.Button(top,text="Inner",command=ProcessButtonInner).grid(row=3,column=5)
bt4 = tk.Button(top,text="Outer",command=ProcessButtonOuter).grid(row=3,column=6)
bt5 = tk.Button(top,text="Quit",command=ProcessButtonQuit,width=10).grid(row=5,column=5,columnspan=2)

top.mainloop()
