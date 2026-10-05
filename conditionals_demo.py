# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:00:28 2024

@author: José Alberto Rocha Munguía
"""

# if / elif / else demo.
# Change ONLY the two variables below, then run:
#   python3 conditionals_demo.py
#
# age < 18              -> "Can't pass through here"
# age 18..59, alive     -> "I'll take the sentence"
# age 18..59, not alive -> "Eternal ZZZ"
# age >= 60             -> "The more wrinkled..."

age = 18          # try: 10, 18, 40, 60
is_alive = True   # try: True or False (only matters if age is 18–59)

if age < 18:
    print("Can't pass through here")
elif age >= 18 and age < 60:
    if is_alive == True:
        print("I'll take the sentence")
    else:
        print("Eternal ZZZ")
else:
    print("The more wrinkled...")