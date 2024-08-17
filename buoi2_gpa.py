# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:20:16 2024

@author: DELL
"""

gpa = float(input("Nhập điểm trung bình"))
if gpa < 3.5:
    print("Học lực Kém")
elif gpa >= 3.5 and gpa < 5.0:
    print("Học lực Yếu")
elif gpa >= 5.0 and gpa < 7.0:
    print("Học lực Trung bình")
elif gpa >= 7.0 and gpa < 8.0:
    print("Học lực Khá")
elif gpa >= 8.0 and gpa < 9.0:
    print("Học lực Giỏi")
else:
    print("Học lực Xuất sắc")
