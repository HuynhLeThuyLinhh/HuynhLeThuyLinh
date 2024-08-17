# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:21:31 2024

@author: DELL
"""

def calculate_taxi_fare(distance):
    # Xác định các mức giá theo quãng đường
    if distance <= 1:
        fare = 20000
    elif distance <= 3:
        fare = 20000 + (distance - 1) * 13000
    elif distance <= 8:
        fare = 20000 + 2 * 13000 + (distance - 3) * 12000
    else:
        fare = 20000 + 2 * 13000 + 5 * 12000 + (distance - 8) * 10000
    
    # Áp dụng giảm giá 8% nếu tổng tiền trên 100.000 VNĐ
    if fare > 100000:
        fare *= 0.92
    
    return fare

# Nhập quãng đường từ người dùng
distance = float(input("Nhập quãng đường đi được (km): "))

# Tính và hiển thị tiền taxi
fare = calculate_taxi_fare(distance)
print(f"Tổng tiền taxi phải trả: {fare:.2f} VNĐ")
5