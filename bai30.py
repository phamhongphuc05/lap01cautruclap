# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:07:22 2024

@author: kid30
"""

n=input("Nhập tháng năm theo định dạng vd(1/2004):")
thang,nam=map(int,n.split("/"))
if nam% 4==0 or nam%400==0:
    if thang==2:
       print("số ngày là 29")
    elif thang==[1,3,5,7,8,10,12]:
        print("số ngày là 31")
    else:
        print("số ngày là 30")
else:
    if thang==2:
       print("số ngày là 28 ")
    elif thang==[1,3,5,7,8,10,12]:
        print("số ngày là 31")
    else:
        print("số ngày là 30")