# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:27:45 2024

@author: kid30
"""

n=int (input("Nhập vào 1 số: "))
for i in range(1,n+1):
   while  i**2==n:
       print(n,"là số chính phương ")
   else:
        n=int (input("Nhập lại vào 1 số: "))
       