from matplotlib import pyplot as plt
import numpy as np
import time

# 创建实时绘制横纵轴变量
x = []
y = []

# 创建绘制实时损失的动态窗口
plt.ion()

# 创建循环
for i in range(100):
    stime=time.time();
    x.append(i);	# 添加i到x轴的数据中
    y.append(i**2);	# 添加i的平方到y轴的数据中
    plt.clf();  # 清除之前画的图
    plt.plot(x,y*np.array([-1]));  # 画出当前x列表和y列表中的值的图形
    plt.pause(0.001);  # 暂停一段时间，不然画的太快会卡住显示不出来
    plt.ioff();  # 关闭画图窗口
    print(time.time()-stime);
