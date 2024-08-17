# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:45:58 2024

@author: DELL
"""

s = input("Nhập ngày, tháng, năm (dd/mm/yyy): ")

try:
    ngày, tháng, năm = map(int, s.split("/"))
except ValueError:
    print("Định dạng ngày không hợp lệ.")
else:
    if năm % 400 == 0 or (năm % 4 == 0 and năm % 100 != 0):
        check = True
    else:
        check = False
    x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check:
        x[1] = 29
    if năm < 1:
        print("Năm không hợp lệ.")
    elif tháng < 1 or tháng > 12:
        print("Tháng không hợp lệ.")
    elif ngày < 1 or ngày > x[tháng -1]:
        print("Ngày không hợp lệ.")
    else:
        print("Ngày, tháng, năm hợp lệ.")
