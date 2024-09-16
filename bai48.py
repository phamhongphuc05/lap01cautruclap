# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:29:58 2024

@author: kid30
"""

ds = []
min_t = float('inf')  # Khởi tạo giá trị nhỏ nhất ban đầu
# Duyệt qua các giá trị của z
for z in range(1, 979 // 9 + 1):
    tim = 979 - 9 * z  # Tính phần còn lại của phương trình
    if tim <= 0:
        break
    
    # Duyệt qua các giá trị của y
    for y in range(1, tim // 7 + 1):
        if (tim - 7 * y) > 0:  # Đảm bảo phần còn lại lớn hơn 0
            x = (tim - 7 * y) / 2  # Tính x từ phương trình
            
            # Kiểm tra nếu x là số nguyên và dương
            if (tim - 7 * y) % 2 == 0 and x > 0:  # Kiểm tra x là số nguyên
                x = int(x)  # Chuyển x thành số nguyên
                tong = x + y + z  # Tính tổng x + y + z
                
                # Kiểm tra xem tổng có nhỏ hơn tổng nhỏ nhất không
                if tong < min_t:
                    min_t = tong
                    ds = [(x, y, z)]  # Reset danh sách nghiệm
                elif tong == min_t:
                    ds += [(x, y, z)]  # Thêm nghiệm 

# In kết quả
print("Các bộ nghiệm nguyên (x, y, z) với x + y + z nhỏ nhất:")
if ds:  # Kiểm tra xem ds có rỗng không
    for i in ds:
        print(i)
else:
    print("Không có bộ nghiệm nào thỏa mãn.")