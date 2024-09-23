# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:00:47 2024

@author: nhuylab01
"""
thang=int(input("Nhap thang:"))
nam=int(input("Nhap vao nam:"))
if thang in [1,3,5,7,8,10,12]:
    ngay=31
elif thang in [4,6,9,11]:
    ngay=30
else:
    if (nam%4==0 and nam%100!=0)or(nam%400==0):
       ngay=29
       print("Nam nhuan")
    else:
       ngay=28
       print("Nam khong nhuan")
print(f"{ngay}, {thang},{nam}")
print(f"Vay thang {thang} co {ngay} ngay.")