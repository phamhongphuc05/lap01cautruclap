# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:24:45 2024

@author: Phạm Hồng Phúc 
"""
a=float(input("Nhập giá trị a:"))
b=float(input("Nhập giá trị b:"))
c=float(input("Nhập giá trị c:3"))
if (a+b)>c and (b+c)>a and (c+a)>b:
    print(" là 3 cạnh của tam giác")
if a==b==c:
    print (" Là tam giác đều")
elif  a==b!=c or a==c!=b or  a!=b==c:
    print (" là tam giác cân")
elif (a**2+b**2)==c**2 or (b**2+c**2)==a**2 or (a**2+c**2)==b**2:
    print("Là tam giác vuông")
else :
    print (" là tam giác thường")
 
    
