# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:58:23 2024

@author: kid30
"""

n=int(input("Nhập số n:"))
S=sum(range(2,n+1,2))
if n>0:
  print(f"Tổng 2+4+6+..+{n} =",S)
else:
  print("Không hợp lệ")