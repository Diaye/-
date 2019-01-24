# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:23:11 2018

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 20, 0.1) 

def f(x):
    return 0.05*x**2 - 3 


plt.figure(figsize=(15,8))
plt.plot(x,f(x),'#006400', linewidth=2.5)
plt.plot([-5,20],[0,0],color='#8B0000',linestyle='-', linewidth=1)
plt.title('Function Image')
plt.axis([-5,20,-5,20])
plt.grid()
plt.show()
print("根据函数图像，在运行框内输入St(a1,a2,c):例如——St(17,20,1e-5)和St(1,4,1e-5) ")

def St(a1,a2,c):
    b = a2 - f(a2)*(a2-a1)/(f(a2)-f(a1)) 
    
    count = 0
    while abs(f(b)) > c:
        b = a2 - f(a2)*(a2-a1)/(f(a2)-f(a1))
        a2 = a1
        a1 = b
        count = count + 1
        print("第",count,"次弦截结果为：",str(b))
        
    print("弦截法迭代总次数为:{}".format(count))
    print("通过弦截法可得到估计参数值为:{}".format(b))
    
St(17,20,1e-5)  #从右边选取两个
St(1,4,1e-5)    #从左边选取两个