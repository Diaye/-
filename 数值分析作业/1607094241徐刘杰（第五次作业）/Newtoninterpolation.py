# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:16:01 2018

@author: Admin

牛顿插值法（引入书上P134例题4-13）
                            插值函数表
                 ———————————————————————————————
                    x   0    1     2      4
                    y   3    6     11     51 
                 ———————————————————————————————

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,10,1)

xn = [0,1,2,4]
fx = [3,6,11,51]  #定义一个三阶
fx1_0 = (fx[1] - fx[0])/(xn[1] - xn[0])
fx2_1 = (fx[2] - fx[1])/(xn[2] - xn[1])
fx3_2 = (fx[3] - fx[2])/(xn[3] - xn[2])
fx2_1_0 = (fx2_1 - fx1_0)/(xn[2] - xn[0])
fx3_2_1 = (fx3_2 - fx2_1)/(xn[3] - xn[1])
fx3_2_1_0 = (fx3_2_1 - fx2_1_0)/(xn[3] - xn[0])

def N_2x(x):
    return fx[0] + fx1_0*(x - xn[0]) + fx2_1_0*(x - xn[0])*(x - xn[1])   
    
def N_3x(x):
    N_2x(x)
    return N_2x(x) + fx3_2_1_0*(x - xn[0])*(x - xn[1] )*(x - xn[2])
    
print("           ********16070942班徐刘杰作业************")

plt.figure(figsize = (8,6))
plt.plot(x,N_2x(x),'r') 
plt.plot(x,N_3x(x),'g')
plt.plot([0,1,2,4],[3,6,11,51],'ro')
plt.scatter(0.5,N_2x(0.5),label="预测函数点",color='b')
plt.title("牛顿插值法")
plt.grid()
plt.show() 

print("      ***********    蓝点为预测函数点     ***********",'\n')
print("      *******红线为二次牛顿插值拟合函数曲线图像*******",'\n')
print("      *******绿线为三次牛顿插值拟合函数曲线图像*******",'\n')
print("      ********     16070942班徐刘杰作业    **********",'\n')
print("二次牛顿插值法得到f(0.5)的值为：{}".format(N_2x(0.5)))
print("三次牛顿插值法得到f(0.5)的值为：{}".format(N_3x(0.5)))


#*********************递归求解*******************
#def three_interpolations(x, y):
#    m = 0
#
#    value = [0, 0, 0, 0, 0]
#    while m < 3:
#    
#        n = 3
#        while n > m:
#            if m == 0:
#                value[n]=((y[n]-y[n-1])/(x[n]-x[n-1]))
#            else:
#                value[n] = (value[j]-value[n-1])/(x[n]-x[n-1-m])
#            n -= 1
#            m += 1
#    return value;
#    
#def calculate_data(x,p):
#    handle = [];
#    for n in x:
#        handle.append(New_3x(n))
#    return handle
#
#p = three_interpolations(x,y)
#
#def N_3x(x):
#    return fx[0] + p[1]*(x - xn[0]) + p[2]*(x - xn[0])*(x - xn[1])+\
#           p[3]*(x - xn[0])*(x - xn[1])*(x - xn[2])
#
       



