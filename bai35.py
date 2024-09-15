# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:18:12 2024

@author: kid30
"""

n=int(input("Nhập số n:"))
S=sum(range(1,n+1,1))
if n>0:
        print("Tổng các số nguyên S=1+2+..+n là:",S)
else:
        print("Không hợp lệ")
        