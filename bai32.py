# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:13:38 2024

@author: kid30
"""

s=float(input("Nhập quãng đường đi:"))
s1=15.000  #1km
s2=13.500 # từ 2km đến 5km
s3=11.000 #từ 6km
s4=0.9 # giảm 10% khi đi 120km
if s<=1:
    print("Giá tiền là:",s1,"ngàn đồng")
elif 2<=s<=5:
    print("Giá tiền là:",s1+s2*(s-1),"ngàn đồng")
elif s>=6:
    print("Giá tiền là:",s1+s2*4+s3*(s-5),"ngàn đồng")
elif s>120:
    print("Giá tiền là:",s4*(s1+s2*4+s3*(s -5)),"ngàn đồng")
    

   