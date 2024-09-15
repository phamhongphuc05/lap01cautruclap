# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:29:07 2024

@author: kid30
"""
 
n=int(input("Nhập giá trị n:")) 
if n>0 :
  S=0 #khởi tạo biến tổng trước khi sử dụng 
  for i in range(1,n+1):
      S += i**2 
  print("Tổng bình phương các số nguyên đến n là:",S )
    