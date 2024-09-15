# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:14:11 2024

@author: kid30
"""

n=float (input("Nhập số bất kì:"))
while n<=1:
    n=float (input("Nhập lại số bất kì:"))
else:
    for i in range (2,(n**0.5)+1,1):
        if n%i==0:
            print("số nguyên tố là ",n)
        else:
            print("ko hop lệ")
            
            