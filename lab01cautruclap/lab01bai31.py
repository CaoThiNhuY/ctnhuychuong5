# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:09:30 2024

@author: nhuylab1
"""

# Nhập ba số nguyên dương
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or a == c or b == c:
        print("Tam giác cân.")
    else:
        # Kiểm tra tam giác vuông
        if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
            print("Tam giác vuông.")
        else:
            print("Tam giác thường.")
else:
    print("Ba cạnh không lập thành tam giác.")
