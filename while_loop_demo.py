# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:38:59 2024

@author: José Alberto Rocha Munguía
"""

# while loop demo.
# Change ONLY the starting counter and the limit, then run:
#   python3 while_loop_demo.py
#
# Prints "is less than: N" while counter < 5 (N = 0, 1, 2, 3, 4).
# Then the while-else runs once: "The while loop has completed its execution"
# Do not remove "counter += 1" or the loop never ends.

counter = 0   # try: 0, 3, 5  (if this is already >= 5, the while body is skipped)

while counter < 5:   # try: 3 or 10 to print fewer / more lines
    print(f"is less than: {counter}")
    # counter = counter + 1
    counter += 1
else:
    print("The while loop has completed its execution")