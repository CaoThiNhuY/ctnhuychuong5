# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:50:07 2024

@author: nhuylab01
"""

n=int(input("Nhap so nguyen duong n: "))
s=0
x=float(input("Nhap so x: "))
while n<=0:
    n=int(input("Nhap lai n: "))
for i in range(1,n+1):
    t=x**i
    m=i+1
    s=x+t/m
print(s)
