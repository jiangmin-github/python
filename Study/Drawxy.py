import numpy as np 
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axt

i = np.linspace(-8,8,1000)

sc = input("please input the equation : ")
sc = sc.replace("sin","np.sin")
sc = sc.replace("cos","np.cos")
sc = sc.replace("tan","np.tan")
sc = sc.replace("exp","np.exp")
sc = sc.replace("sqrt","np.sqrt")
sc = sc[0:4] + '[' + sc[4:] + ' for x in i]'
print(sc)
scope={}
exec(sc)

#创建画布
fig = plt.figure()

#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axt.Subplot(fig, 111)

#将绘图区对象添加到画布中
fig.add_axes(ax)
    
# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)

# 添加x坐标轴，加上箭头
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.5)

# 添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.5)

# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

xmax = np.max(i)
xmin = np.min(i)
ymax = np.max(y)
ymin = np.min(y)

ax.set_xlim(xmin-0.3,xmax+0.3)
ax.set_ylim(ymin-0.3,ymax+0.3)

plt.plot(i,y)

plt.show()
