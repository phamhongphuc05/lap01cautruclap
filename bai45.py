# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:17:29 2024

@author: kid30
"""

n=int(input("Nhập n:"))
x=int(input("Nhập x:"))
tong=0 
sum_k=0 
for k in range(1,n+1):
    sum_k += k
    term= (x**k)/sum_k
    tong+=term
print(tong)