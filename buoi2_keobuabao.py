# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:18:20 2024

@author: DELL
"""

import random

def get_machine_choice():
    choices = ["Kéo", "Búa", "Bao"]
    return random.choice(choices)

def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return "Hòa"
    elif (user_choice == "Kéo" and machine_choice == "Bao") or \
         (user_choice == "Búa" and machine_choice == "Kéo") or \
         (user_choice == "Bao" and machine_choice == "Búa"):
        return "Bạn thắng"
    else:
        return "Máy thắng"

def main():
    print("Chào mừng bạn đến với trò chơi Kéo - Búa - Bao!")
    print("Lựa chọn của bạn: Kéo, Búa, Bao")
    
    user_choice = input("Nhập lựa chọn của bạn: ").strip()
    
    if user_choice not in ["Kéo", "Búa", "Bao"]:
        print("Lựa chọn không hợp lệ! Vui lòng nhập Kéo, Búa, hoặc Bao.")
        return
    
    machine_choice = get_machine_choice()
    print(f"Máy chọn: {machine_choice}")
    
    result = determine_winner(user_choice, machine_choice)
    print(result)

if __name__ == "__main__":
    main()
