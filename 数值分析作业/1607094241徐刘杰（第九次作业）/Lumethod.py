# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 08:59:16 2018

@author: Admin

目的：对矩阵matrix进行LU分解

原理：LU分解是一行一行进行分解的，所以使用过的行可以被LU矩阵中的值所代替。

引自书上P74 例3-8

"""

matrix = [[2, 2, 3], [4, 7, 7], [-2, 4, 5]]

i = 0
size = len(matrix)
while i < size:
    if i == 0:
        j = 1
        while j < size:
            matrix[j][0] = int(matrix[j][0]/matrix[0][0])  #用int型强制去小数点，否则输出为0.0型
            j += 1
    else:
        j = i                 #计算U矩阵，计算过程是求一列U矩阵
        while j < size:
            sum_u = 0
            flag_u = i - 1
            while flag_u > -1:
                if j == i:
                    sum_u += int(matrix[flag_u][j]*matrix[j][flag_u])
                else:
                    sum_u += int(matrix[flag_u][j]*matrix[j-1][flag_u])
                flag_u -= 1
            matrix[i][j] = matrix[i][j] - sum_u
            j += 1
            
        j = i+1              #计算L矩阵，计算过程是求一列L矩阵
        while j < size:
            sum_L = 0
            flag_L = i-1
            while flag_L > -1:
                sum_L += int(matrix[i][flag_L]*matrix[j][flag_L])   
                flag_L -= 1
            matrix[j][i] = int((matrix[j][i]-sum_L)/matrix[i][i])
            j += 1
    i += 1
 
'''输出L,U矩阵'''
L = []
U = []
b = 0
while b < size:
    a = 0
    array1 = []
    array2 = []
    while a < size:
        if b == a :
            array1.append(1)
            array2.append((matrix[b][a]))
        elif b > a:
            array1.append(matrix[b][a])
            array2.append(0)
        else:
            array1.append(0)
            array2.append(matrix[b][a])
        a += 1
    L.append(array1)
    U.append(array2)
    b += 1
    
print("*****16070942班徐刘杰作业*****\n")
print("L矩阵为：")
for l in L:
    print("\t",l)
print("\n")
print("U矩阵为：")
for u in U:
    print("\t",u)



