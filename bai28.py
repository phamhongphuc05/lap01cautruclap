# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:41:41 2024

@author: kid30
"""

n=int(input ("Nhấp giá trị n:"))
while n<0:
    n=int(float ("Nhấp lại giá trị:"))
else:
    print("giá trị n là:")
for i in range(1,n+1,1):
  divisors=[]
  if n%i==0 :
     print (i,end=",")
     
          