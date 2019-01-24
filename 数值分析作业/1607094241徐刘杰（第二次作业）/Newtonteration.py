# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:59:05 2018

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10) 

def f(x):
    return 0.8*x**2 - 3 
    
def df(x):
    return 1.6*x

plt.figure(figsize=(10,6))
plt.plot(x,f(x),'#006400', linewidth=2.5)
plt.plot([0,10],[0,0],color='#8B0000',linestyle='-', linewidth=1)
plt.title("Newton teration method")
plt.axis([0,10,-5,30])
plt.grid()
plt.show()
print("根据函数图像，在运行框内输入Newton(x,b): 例如——Newton(8,1e-10)")
 
def Newton(x1,b):
    count = 0
    x = 0
    while abs(f(x)) > b:
        x = x1 - (f(x1)/df(x1))        
        count = count + 1
        plt.plot([x, x1], [0, f(x)],"r", linewidth=1)
        x1 = x
        print("第",count,"次牛顿切线结果为：",str(x))
        
    print("牛顿切线法迭代总次数为:{}".format(count))
    print("牛顿切线法得到的根为:{}".format(x))
    print("切线效果图如下图所示：")

Newton(8,1e-10)    #从右边开始切线


