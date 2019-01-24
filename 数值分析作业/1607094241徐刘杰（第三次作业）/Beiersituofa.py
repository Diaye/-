# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:32:45 2018

@author: Admin
"""
 
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1) 

def f(x):
    return  2.5*x**5 - 1.5*x**4 - x**3 + 6.25*x**2 -4.65*x - 2

plt.figure(figsize=(10,6))
plt.plot(x,f(x),'#006400', linewidth=1)
plt.plot([-5,10],[0,0],color='#8B0000',linestyle='--', linewidth=1.5)
plt.title("Function Image")
plt.axis([-4,4,-5,10])
plt.grid()
plt.show()
print("              ************运行结果分析****************")

a = [-2,-4.65,6.25,-1,-1.5,2.5]     
b = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5']
c = ['c0','c1','c2','c3','c4','c5']
rs = [-2,-1,'r','s']                 
error = ['%r','%s']                    
x = ['x1','x2','x3','x4','x5']

def C(r,s):
    c[5] = b[5]
    c[4] = b[4] + r*c[5]
    i = 3
    while i != -1:
        c[i] = round(b[i] + r*c[i+1] + s*c[i+2],4)
        i = i - 1
        
def B(r,s):
    b[5] = a[5]           
    b[4] = a[4] + r*b[5]
    i = 3
    while i != -1:
        b[i] = round(a[i] + r*b[i+1] + s*b[i+2],4)
        i = i - 1

def Operation():
    r = (b[0]*c[3] - b[1]*c[2])/(c[2]*c[2] - c[1]*c[3]) + rs[0]
    s = (b[0]*c[2] - b[1]*c[1])/(c[3]*c[1] - c[2]*c[2]) + rs[1]
    rs[2],rs[3] = r,s

def Error():
    error[0] = round((rs[2] - rs[0])/rs[2],4)
    error[1] = round((rs[3] - rs[1])/rs[3],4)
    rs[0], rs[1] = rs[2],rs[3]

t = 0
p = 0
q = 0
count = 0
item = 0 
item1 = [4,1]                              
def Bellstofa(r,s):
    global item,t,p,count
    B(r, s)
    C(r, s)
    Operation()
    Error()
    count = count + 1
    if (abs(error[0]) < 1e-3) or (abs(error[1]) < 1e-3): 
        print("多项式函数经过",count,"次迭代得到估计根值为：")
        x[p] = (rs[2] - (rs[2]**2 + 4*rs[3])**(1/2))/2  
        print("x",p,"=",x[p])
        p = p + 1
        
        x[p] = (rs[2] + (rs[2]**2 + 4*rs[3])**(1/2))/2 
        print("x",p,"=",x[p])
        p = p + 1
        item = item1[t]                          
        t = t + 1
        if item == 1:
            x[4] = round((-rs[2]) / rs[3] , 0)  
            print("x", 4, "=", x[4])
            print("由贝尔斯托法求得多项式函数的根为（实数根、复数根）:")
            print("{}".format(x))
        elif (item >= 2):                                 
            a[0],a[1],a[2],a[3],a[4],a[5] = b[2],b[3],b[4],b[5],0,0
            Bellstofa(rs[2], rs[3])
    else:
        Bellstofa(rs[2],rs[3])                  

Bellstofa(-2,-1)
