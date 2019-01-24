# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:55:38 2018

@author: Admin
"""

"""
   三元一次方程组：              矩阵：
   2x1 - x2 + 3x3 = 1           2  -1   3   1
   4x1 + 2x2 + 5x3 = 4          4   2   5   4
   x1 + 2x2 + x3 = 7            1   2   1   7
   
"""
 
def Gaussianelimination(figure):       #定义高斯消去法
    
    m_len = len(figure)                #行数
    n = 0                              #循环次数

    ''' 1、 将行列式转换成上三角的行列式'''
    while n < m_len - 1:
        m = figure[n]                 #m表示行的数据
        a1 = m[n]                     #a1表示某一行
        b1 = []
        for x in m:
            x = x / a1
            b1.append(x)
        figure[n] = b1
 
        row = n + 1                  # row表示可以消元的行数
        while row < m_len:
            b2 = []
            a2 = figure[row][n]
            i = 0
            for x1 in figure[row]:
                if x1 != 0:
                    x1 = x1 - (a2 * b1[i])
                    b2.append(x1)
                else:
                    b2.append(0)
                i += 1
            figure[row] = b2
            row += 1
        n += 1
 
        
    '''2、求解'''
    values = []                   # 求值并用数组values存储
    i = m_len - 1
    row_n = 0
    column = len(figure[0])
    column1 = column - 2         # 要除的列
    while i > -1:
        Evaluate_m = figure[i]
        if i == m_len - 1:
            value = Evaluate_m[column - 1] / Evaluate_m[column1]
            values.append(value)
        else:
            row_n = (column - column1 - 2)
            a2 = Evaluate_m[column - 1]
            
            row_of_result = 0
            while row_n > 0:
                a2 -= Evaluate_m[column1 + row_n] * values[row_of_result]
                row_of_result += 1
                row_n -= 1
            value = a2 / Evaluate_m[column1]
            values.append(value)
        column1 -= 1
        i -= 1
    return values
 
values = [[2,-1,3,1], [4,2,5,4], [1,2,1,7]]       #矩阵数据
root = Gaussianelimination(values)                #调用Gaussianelimination（）

print("*****1607094241徐刘杰*******\n")
print("由高斯消去法得到方程组的解为:\n",\
        "x1 = {}".format(str(root[0])) \
      + "  x2 = {}".format(str(root[1])) \
      + "  x3 = {}".format(str(root[2])))