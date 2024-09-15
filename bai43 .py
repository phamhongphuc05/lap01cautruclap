# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:35:04 2024

@author: kid30
"""

n=int(input("Nhập n:"))
S=0
for i in range(1,n+1):
    S+=i/(i+1)
print("1/2+2/3+..+ n/n+1",S)
