# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:55:36 2024

@author: José Alberto Rocha Munguía
"""

# Function demo: int() and modulo (%).
# Change `number` (and the modulo_calc line if you uncomment it), then run:
#   python3 math_functions_demo.py
#
# ocean_wave(1.3) prints: "The integer associated with 1.3 is: 1"
# modulo_calc is defined but not called until you uncomment the last line.

def ocean_wave(a):
    # a should be a number; int() drops the decimal part (1.3 -> 1)
    b = int(a)
    print(f"The integer associated with {a} is: {b}")
    return b

# MODULO function
def modulo_calc(chocokrispis, zucaritas):
    # Cereal names are just the two operands: left % right
    corn_pops = chocokrispis % zucaritas
    print(f"{chocokrispis} modulo {zucaritas} is: {corn_pops}")
    return corn_pops

number = 1.3   # try: 1.3, 4.9, -2.7
ocean_wave(number)
# modulo_calc(10, 3)   # uncomment -> "10 modulo 3 is: 1"
