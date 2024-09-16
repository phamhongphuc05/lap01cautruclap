# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:49:47 2024

@author: kid30
"""

target_sum=979 
solutions = []
max_sum = 0
for x in range(1, target_sum // 2 + 1):
        for y in range(1, (target_sum - 2 * x) // 7 + 1):
            for z in range(1, (target_sum - 2 * x - 7 * y) // 9 + 1):
                # Kiểm tra điều kiện phương trình
                if 2 * x + 7 * y + 9 * z == target_sum:
                    sumxyz=x+y+z 
                    if sumxyz > max_sum:
                       max_sum = sumxyz
                       solutions = [(x, y, z)]
                    elif sumxyz == max_sum:
                       solutions.append((x, y, z))
print( solutions, end="\t")
