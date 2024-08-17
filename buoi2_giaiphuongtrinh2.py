# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:50:17 2024

@author: DELL
"""

a = float(input("Nhập a ="))
b = float(input("Nhập b ="))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Ngiệm của phương trình là x =", (-b/a))