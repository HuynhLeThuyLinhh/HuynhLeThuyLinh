# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:21:31 2024

@author: DELL
"""

#Tính tiền taxi theo số km quãng đường đi được:
a = float (input("Số km quãng đường đi được: "))
if a==1:
    print("Tiền taxi theo số km quãng đường đi được: ",20,"k")
elif a<=3:
    print("Tiền taxi theo số km quãng đường đi được: ", a*13,"k")
elif a<=8:
    print("Tiền taxi theo số km quãng đường đi được: ", 3*13+(a-3)*12,"k")
else:
    b = 3*13+5*12+(a-8)*10
    if b <= 100: 
        print("Tiền taxi theo số km quãng đường đi được: ", b,"k")
    else:
        print("Tiền taxi theo số km quãng đường đi được: ", b*0.92,"k")