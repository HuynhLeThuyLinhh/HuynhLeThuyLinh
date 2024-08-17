# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:45:58 2024

@author: DELL
"""

from datetime import datetime

def is_valid_date(date_str):
    for fmt in ('%d/%m/%Y', '%d-%m-%Y'):
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False

# Nhập ngày tháng năm từ người dùng
date_input = input("Nhập ngày tháng năm (dd/mm/yyyy hoặc dd-mm-yyyy): ")

# Kiểm tra tính hợp lệ
if is_valid_date(date_input):
    print("Ngày tháng năm hợp lệ.")
else:
    print("Ngày tháng năm không hợp lệ.")
