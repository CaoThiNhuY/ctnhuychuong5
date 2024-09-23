# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:13:49 2024

@author: lab01-lap-nhuy
"""

n=int(input("Nhap so nguyen duong N"))

# Biến để lưu kết quả
kết_quả = 0

# Vòng lặp kiểm tra
for i in range(1, n + 1):
    if i * i == n:
        kết_quả = 1  # Đánh dấu là số chính phương
        break

# Kết quả
if kết_quả == 1:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
