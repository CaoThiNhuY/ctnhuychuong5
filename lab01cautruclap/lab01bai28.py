# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:02:25 2024

@author: lab01
"""

n=int(input("Nhap so nguyen duong N:"))
while n<0:
    print("Nhap lai n")
#In uoc so
print("Cac uoc so cua n la: ")
for i in range (1,n+1):
    if n%i==0:
        print(i, end="\t")
    

