# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:17:17 2024

@author: DELL
"""

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    
    if a == b == c:
        print("Day la tam giac deu.")
    elif a**2 + b**2 == c**2:
        print("Day la tam giac vuong.")
    elif a == b or b == c or a == c:
        print("Day la tam giac can.")
    else:
        print("Day la tam giac thuong.")
else:
    print("a,b,c khong phai la ba canh cua mot tam giac.")
