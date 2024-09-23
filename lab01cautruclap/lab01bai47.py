# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:01:38 2024

@author: nhuylab01
"""

danhsach=[]
max=0
for x in range(1,490): # 979/2
    for y in range(1,140): #979/7
        for z in range(1,109):
           if 2*x + 7*y + 9*z == 979:
               sum= x+y+z
               if sum > min:
                   max=sum
                   danhsach=[(x,y,z)]
print(f"{danhsach} với bộ nghiệm (x+y+z)={max}")  