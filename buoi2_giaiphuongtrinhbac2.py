# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:54:09 2024

@author: DELL
"""

a = float(input("Nhập số a (a < > 0): "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta = b*b - 4*a*c
if delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 =", -b/(2*a))
if delta > 0:
    print("Phương trình có 2 nghiệm x1 =", (-b + delta**0.5)/(2*a),
          "x2 =", (-b - delta**0.5)/(2*a))
if delta < 0:
    print("Phương trình đã cho vô nghiệm ! ")