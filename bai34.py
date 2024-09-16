# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:14:11 2024

@author: kid30
"""
            
n = int(input("Nhập vào số nguyên dương n: "))
if n<2:
    print(" N không phải số nguyên tố.")
for i in range (2,int(n**0.5) + 1):
    if n % i ==0:
        print(n, "không là sô nguyên tố")
        break
    else:
     print(n,"là số nguyên tố")
     break            