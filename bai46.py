# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:37:27 2024

@author: kid30
"""

target_sum=int(input("Nhập số đề bài cho:"))
solutions = []
for x in range(1, target_sum // 2 + 1):
        for y in range(1, (target_sum - 2 * x) // 7 + 1):
            for z in range(1, (target_sum - 2 * x - 7 * y) // 9 + 1):
                # Kiểm tra điều kiện phương trình
                if 2 * x + 7 * y + 9 * z == target_sum:
                    solutions.append((x, y, z))
print( solutions, end="\t")
