# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:19:44 2021

"""

x = 1
y = 1
prev_ans = 1

while x < 526:
    ans = x * y + prev_ans + 3
    x += 1
    y += 1
    prev_ans = ans

print('x = ' + str(x))
print('ans = ' + str(ans))