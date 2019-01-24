# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:17:24 2018

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8, 0.1) 

#H(x) = (10*x - 3)**(1/3) - x

def f(x):
    return (10*x - 3)**(1/3)  
def g(x):
    return x
a = 0
plt.figure(figsize=(15,8))
plt.plot(x,f(x),'#006400', linewidth=1)
plt.plot(x,g(x),color='#8B0000', linewidth=1.5)
plt.title('Function Image')
plt.axis([1,8,1,8])
plt.grid()
plt.show()
print("根据函数图像，在运行框内输入iteration(a,b):例如——iteration(4,1e-5) 和iteration(2,1e-5)")

#迭代法
def iteration(a,b):
    count = 0
    if f(a)==g(a):
        print("由迭代法可知函数的根解为：{}".format(a))
        return
    else:
        while (abs(f(a) - g(a)) > b):
            a = f(a)
            count = count + 1
            plt.scatter([a, f(a), f(a)], [f(a), f(a), f(f(a))], color = 'b')
            plt.plot([a, f(a)], [f(a), f(a)], color = 'r')
            plt.plot([f(a), f(a)], [f(a),f(f(a))], color = 'r')
            print("第",count,"次简单迭代结果为：",str(a))
    print("迭代总次数为:{}".format(count))         
    print("由简单迭代法可知函数A的根解为：{}".format(a))
    print("简单迭代效果图如下图所示：")
    
iteration(4,1e-5)   #从右边输入
iteration(2,1e-5)   #从左边输入
            
            