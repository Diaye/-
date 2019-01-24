# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:12:06 2018

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,15,0.1)

x = [3,4.5,7,9]
y = [2.5,1,2.5,0.5]

plt.title("一次样条函数图像")
plt.plot(x,y,'b')
plt.scatter(x,y,color='r')
plt.grid()
plt.show()

print("********  16070942班 徐刘杰 作业 *********")

#共有四个数据点，3个区间，所以必须确定3x3=9个未知数
#相邻多项式在内部结点处的函数数值必须相等

#a = [a1,a2,a3]
#b = [b1,b2,b3]
#c = [c1,c2,c3]
#def Prototype(xn):
#    i = 0
#    a[0] = 0
#    while i < len(xn)-1:
#        a[i]*xn[i]**2 + b[i]*x[i] + c[i] = fx[i]
#        a[i]*xn[i+1]**2 + b[i]*x[i+1] + c[i] = fx[i+1]
#        2*xn[i+1]*a[i] + b[i] = 2*xn[i+1]*a[i+1] + b[i+1]
#        i += 1
 
"""
将所有方程的参数（系数）进行输入,形成矩阵
20.25a1 + 4.5b1 + c1 = 1
20.25a2 + 4.5b2 + c2 = 1
49a2 + 7b2 + c2 =2.5
49a3 + 7b3 + c3 =2.5
9a1 + 3b1 + c1 = 2.5
81a3 + 9b3 +c3 = 0.5
9a1 + b1 = 9a2 + b2
14a2 +b2 = 14a3 + b3
a1 = 0 

由上面9个条件中的系数可得到两个矩阵Array1和Array2
 
              Array1
              
4.5   1    0    0    0    0    0    0
 0    0  20.25 4.5   1    0    0    0
 0    0    49   7    1    0    0    0
 0    0    0    0    0    49   7    1
 3    1    0    0    0    0    0    0
 0    0    0    0    0    81   9    1
 1    0   -9   -1    0    0    0    0
 0    0   14    1    0   -14  -1    0
 
             Array2
             
               1
               1
              2.5
              2.5
              2.5
              0.5
               0
               0
 
"""  

'''先初始化为0数组'''
def init(n):
    m = 0;
    array = []
    while m < n:
        array.append(0)
        m += 1
    return array
    
'''思路：用一个数组shuzu = []存放参数'''   
def Prototype(x):
    shuzu = []
    i = 1
    while i < 3:
        array = init(9)
        array[(i-1)*3]=x[i]*x[i]
        array[(i-1)*3+1]=x[i]
        array[(i-1)*3+2]=1
        array1 =init(9)
        array1[i * 3] = x[i] * x[i]
        array1[i * 3 + 1] = x[i]
        array1[i * 3 + 2] = 1
        temp = array[1:]
        shuzu.append(temp)
        temp = array1[1:]
        shuzu.append(temp)
        i += 1

    array = init(8)
    array[0] = x[0]
    array[1] = 1
    shuzu.append(array)
    array = init(9)
    array[6] = x[3] **2
    array[7] = x[3]
    array[8] = 1
    temp = array[1:]
    shuzu.append(temp)
    
    i = 1
    while i < 3:
        array = init(9)
        array[3*(i - 1) ] = 2*x[i]
        array[3*(i - 1) + 1] = 1
        array[3*i] = -2*x[i]
        array[3*i + 1] = -1
        temp = array[1:]
        shuzu.append(temp)
        i += 1
        
    return shuzu

'''用solve方法解决矩阵求每段区间二阶函数的系数'''
def coefficient(k,y):
    answer = init(8)
    i = 1
    while i < 3:
        answer[(i-1)*2] = y[i]
        answer[(i-1)*2+1] = y[i]
        i += 1
    answer[4] = y[0]
    answer[5] = y[3]
    Array1 = np.array(Prototype(x))  
    Array2 = np.array(answer)
    return np.linalg.solve(Array1,Array2)

def Parsing(k,x):     #k为二次样条曲线的系数值
    answer = []
    for mx in x:
        answer.append(k[0]*mx**2 + k[1]*mx + k[2])
    return  answer

curvex = []
curvey = []
answer = coefficient(Prototype(x),y)

'''[3,4.5]区间的函数图像，直线'''
curvex1 = np.arange(3, 4.5, 0.01)
curvey1 = Parsing([0,answer[0],answer[1]],curvex1)
curvex.extend(curvex1)
curvey.extend(curvey1)

'''[4.5,7]区间的函数图像，二次样条曲线1'''
curvex2 = np.arange(4.5, 7, 0.01)
curvey2 = Parsing([answer[2],answer[3],answer[4]],curvex2)
curvex.extend(curvex2)
curvey.extend(curvey2)

'''[7,9]区间的函数图像，二次样条曲线2'''
curvex3 = np.arange(7, 9, 0.01)
curvey3 = Parsing([answer[5],answer[6],answer[7]],curvex3)
curvex.extend(curvex3)
curvey.extend(curvey3)   
    
def  Draw(mx,my,curvex,curvey):       #绘制二次样条函数图像
        plt.title("二次样条函数图像")
        plt.plot(curvex, curvey, color='b')
        plt.scatter(mx,my, color='r')
        plt.grid()
        plt.show()

Draw(x,y,curvex,curvey)
print("********  16070942班 徐刘杰 作业 *********",'\n')

"""
总结:(1)连接前两个点的是直线；(2)最后一个区间上的样条
函数看起来凸出得太高。(3)一次样条和二次样条函数差距还是有点大

内部和相邻的点都在函数上，可以确定6个条件
a[0]*xn[0]**2 +b[0]*x[0] +c[0] = fx[0] 
a[1]*xn[1]**2 +b[1]*x[1] +c[1] = fx[1]
a[2]*xn[2]**2 +b[2]*x[2] +c[2] = fx[2]  
  
a[0]*xn[1]**2 +b[0]*x[1] +c[0] = fx[1]  
a[1]*xn[2]**2 +b[1]*x[2] +c[1] = fx[2]  
a[2]*xn[3]**2 +b[2]*x[3] +c[2] = fx[3]  

导数的连续性，可以确定2个条件
2*xn[1]*a[0] + b[0] = 2*xn[1]*a[1] + b[1]
2*xn[2]*a[1] + b[1] = 2*xn[2]*a[2] + b[2]

假设在第一个节点处的二阶导数为0，所以a[0] = 0
a[0] = 0
"""
