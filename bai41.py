# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:13:53 2024

@author: kid30
"""

n=int(input("Nhập số n:"))
S=0
for i in range(1,2*n+2,2):
    S+=1/i
print(f"S=1+1/3+..+1/(2*{n}+1)=",S)