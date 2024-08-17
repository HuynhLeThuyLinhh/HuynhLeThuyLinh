# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:03:11 2024

@author: DELL
"""

a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("Nhap c : "))
if a+b>c and a+c>b and b+c>a:
    if a==b or a==c or b==c:
        if a==c==b:
            print("Day la ba canh cua tam giac deu")
        else:
            print("Day la ba canh cua tam giac can")
    elif (a**2)+(b**2)==c**2 or (a**2)+(c**2)==b**2 or (c**2)+(b**2)==a**2:
        print("Day la ba canh cua tam giac vuong")
    else:
        pass
else:
    print("Day khong phai ba canh cua tam giac")