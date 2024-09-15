# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:58:18 2024

@author: kid30
"""

n=int(input("Nhập n:"))
S=0 
for i in range(1,n+1):
  S+=1/i
print("S=1+ 1/2 + 1/3+..+ 1/n =",S)
 