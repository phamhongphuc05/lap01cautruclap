# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:23:14 2024

@author: kid30
"""

n=int(input("Nhập n:"))
S=0 
for i in range(1,n+1):
   S+=1/(i*(i+1))
print("S=1+1/n*(n+1)")
    