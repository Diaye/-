# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:41:17 2018

@author: Admin
二分法和试位法求解如下
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 8, 0.1) 

def f(x):
    return 0.5*x**3 - x**2- x - 12

plt.plot(x,f(x),'#006400', linewidth=1.5)
plt.plot([-2,8],[0,0],color='#8B0000',linestyle='--', linewidth=3)
plt.title('Function Image')
plt.grid()
plt.show()

#二分法
def erfen(left, right):
    middle = (left + right)/2
    if  right - left < 1e-5:
        print("二分法估计值的范围为[{},{}]".format(left,right))
        print("二分法估计值为:{}".format(middle))
        return
    elif f(left) == 0:                
          print("二分法估计值为：{}".format(left))
          return
    elif f(right) == 0:                
          print("二分法估计值为：{}".format(right))
          return
    temp1 = f(middle)*f(left)
    temp2 = f(middle)*f(right)
    if temp1 < 0:
        erfen(left, middle)
    elif temp2 < 0:
        erfen(middle, right)
    elif temp1 == 0 :
        if temp2 == 0 :
            print("二分法估计值为{}".format(middle))      
    else :
            print("这个范围内没有实数根！")
          
            
#x = np.arange(-2, 8, 0.1) 
#
#def f(x):
#    return 0.5*x**3 - x**2- x - 12
#
#plt.plot(x,f(x))
#plt.grid()
#plt.show()

#试位法
def shiwei(left,right):
    x = right-(f(right)*(left-right))/(f(left)-f(right))
    if f(x)*f(left) > 0 and f(x)*f(right) > 0:
        print("这个范围内没有实数根！请重新输入约束值！")
        return
    elif f(left) == 0:
        print("试位法的估计解为:{}".format(left))
        return
    elif f(right) == 0:
        print("试位法的估计解为:{}".format(right))
        return
    for i in np.arange(500):             #结束的约束条件
        middle = (left + right)/2
        if f(middle) == 0:
            print ("试位法的估计解为:{}".format(middle))
            return
        elif f(x)*f(left) < 0:    
            right = x
        elif f(x)*f(left) > 0:    
            left = x
    print ("试位法的估计解范围为：[{},{}]".format(left,right))
    print ("试位法估计解为:{}".format(left))
    
while True:
    print("\n****按“1”使用二分法****\n****按“2”使用试位法****\n****按“3”退出程序******")
    judge = int(input())
    if judge != 1 and judge != 2 or judge == 3:
       print ("程序已退出，请重新启动应用！")
       break

    left = float(input("根据函数图，输入左边约束值:"))
    right= float(input("根据函数图，输入右边约束值:"))
    if judge == 1:
       erfen(left, right)
    elif judge == 2:
       shiwei(left,right)

            

        
        

