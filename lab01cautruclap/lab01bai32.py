# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:07:23 2024

@author: lab01-lap
"""

sokm=float(input("Quang duong di dc (km): "))
tong=0
if sokm==1:
    tong=sokm*15000
elif 2<=sokm<=5:
    tong=15000+(sokm-1)*13500
elif sokm >= 6:
    tong= 15000+(sokm-4)*13500 + sokm*11000
elif sokm > 120:
    tong=(15000+(sokm-4)*13500+ sokm*11000)*0.9
print("so km da di la: ",sokm,"va so tien phai tra la:",tong)
