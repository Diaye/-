# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:20:20 2018

@author: Admin

拉格朗日插值法（引入书上P137例题4-13）
                             插值函数表
                 ———————————————————————————————
                    x   0    1     2      4
                    y   3    6     11     51 
                 ———————————————————————————————

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  
font_set = FontProperties(fname=r"C:\Windows\Fonts\SimSun.ttc", size=16)  

x = np.arange(-5,10,1)

xn = [0,1,2,4]
fx = [3,6,11,51]


#**********************原始方法(较繁琐）**********************************
#x0_i = (xn[0] - xn[1])*(xn[0] - xn[2])*(xn[0] - xn[3])
#x1_i = (xn[1] - xn[0])*(xn[1] - xn[2])*(xn[1] - xn[3])
#x2_i = (xn[2] - xn[0])*(xn[2] - xn[1])*(xn[2] - xn[3])
#x3_i = (xn[3] - xn[0])*(xn[3] - xn[1])*(xn[3] - xn[2])
#
#
#def Larange(x):
#    return fx[0]*((x - 1)*(x - 2)*(x - 4))/x0_i + fx[1]*((x - 0)*(x - 2)*(x - 4))/x1_i +\
#fx[2]*((x - 0)*(x - 1)*(x - 4))/x2_i + fx[3]*((x - 0)*(x - 1)*(x - 2))/x3_i


#**********************使用循环（较简易）*********************************
def Larange(x):
    n = 0
    for i in range(len(fx)):
        a = fx[i]
        for j in range(len(fx)):
            if i != j:
                a *= (x-xn[j])/(xn[i]-xn[j])
        n += a       #注意此处的位置
    return n
    
print("           ********16070942班徐刘杰作业************")

plt.figure(figsize = (8,6)) 
plt.plot(x,Larange(x),'g')
plt.plot([0,1,2,4],[3,6,11,51],'ro')
plt.scatter(0.5,Larange(0.5),label="预测函数点",color='b')
plt.title("拉格朗日插值法",fontproperties=font_set)
plt.legend(("Fitting image curve", "Raw data point","Prediction point"),loc='best')
plt.grid()
plt.show() 

print("      ***********    红点为原始函数点     ***********",'\n')
print("      ***********    蓝点为预测函数点     ***********",'\n')
print("      *******绿线为拉格朗日插值拟合函数曲线图像*******",'\n')
print("      ********     16070942班徐刘杰作业    **********",'\n')
print("拉格朗日插值法得到f(0.5)的值为：{}".format(Larange(0.5)))


