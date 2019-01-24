# -*- coding: utf-8 -*-
"""
Created on Sun Dec 2 14:37:09 2018

@author: Admin
"""

import numpy as np
import matplotlib.pyplot  as plt

x = np.arange(-0.5,1.5,0.05)

def f(x):
    global a,b
    return a + b*x
plt.figure(figsize = (8,6)) 
plt.plot(x,f(x))
plt.plot([0.0, 0.2,0.4,0.6,0.8],[0.9,1.9,2.8,3.3,4.2],'ro')
plt.grid()
plt.show() 


i = 0
x = [0.0,0.2,0.4,0.6,0.8]
y = [0.9,1.9,2.8,3.3,4.2]

xsum = sum(x)
ysum = sum(y)
avgx = xsum/len(x)     
avgy = ysum/len(y)
nxy = len(x) * avgx * avgy
x2 = len(x) * ((avgx)**2)

xxsum = 0
xysum = 0
for i in range(len(x)):
    xxsum = x[i]*x[i] + xxsum
for i in range(len(y)):
    xysum = x[i]*y[i] + xysum

b = round((xysum - nxy)/(xxsum - x2),5)
a = round(avgy - b * avgx,5)
print("         ********最小二乘法拟合直线图**********",'\n')
print("最小二乘法得到a值为：{}".format(a))
print("最小二乘法得到b值为：{}".format(b))
print("最小二乘法得到直线方程为：y = ",a," + ",b,"x")




    
    
