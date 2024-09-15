# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:01:29 2024

@author: kid30
"""

n=int(input("Nhập số n:"))
N=1  #khoitao nhân N với từng số từ 1 đến n 
if n>0: 
  for i in range(1,n+1):
    N*= i 
  print(f"tích các số từ 1 đến {n}= ",N)
else:
    print("Không hợp lệ")

    