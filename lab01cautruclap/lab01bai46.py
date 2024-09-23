# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:42:12 2024

@author: labo1nhuy
"""
danhsach=[]
for x in range(1,490): # 979/2
    for y in range(1,140): #979/7
        for z in range(1,109):
           danhsach+=[(x,y,z)]
for i in danhsach:
    print("Bộ nghiệm ",i)
#kiểm tra điều kiện của x,y,z
while x<=0 and y<=0 and z<=0:
    print("Không hợp lệ")