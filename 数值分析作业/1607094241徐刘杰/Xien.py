# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 10:48:28 2019

@author: Admin

欧拉法改进——修恩法

区间[-4，-2]

"""

import numpy as np
import matplotlib.pyplot  as plt

x = np.arange(-4.1,-1.1,0.1)

def f(x):

    return 4*x**3 - 2*x**2 + 3*x + 2
    
def f1(x):
    
    return 12*x**2 - 4*x + 3
    
def g1(x):
    f1(x)
    return f1(-4)*(x +  4) + f(-4)
  
def g2(x):
    f1(x)
    return f1(-2)*(x +  2) + f(-2)
    
def g3(x):
    k = (f1(-4)+f1(-2))/2
    mid = -3                                       #-4和-2的中间值
    return k*(x - mid) + f(mid)  
    
plt.figure(figsize = (8,6)) 
plt.plot(x,f(x))
plt.plot(x,g1(x))
plt.plot(x,g2(x))
'''修正后取斜率为k,且过中值点（-3，f(-3))，做直线'''
plt.plot(x,g3(x),linewidth = 2,linestyle='--')    #修正后取斜率的中值过（-3，f(-3))
plt.plot([-4,-2,-2,-3],[f(-4),f(-2),g1(-2),f(-3)],'ro')
plt.grid()
plt.show() 
print("           ********1607094241徐刘杰作业********")
