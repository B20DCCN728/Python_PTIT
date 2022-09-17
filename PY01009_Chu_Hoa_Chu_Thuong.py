import array as arr
from array import * 

s = str(input())
num_1 = 0
num_2 = 0
for i in range(0, len(s)):
    if s[i] >= 'A' and s[i] <= 'Z': num_1 += 1
    else: num_2 += 1
if num_2 >= num_1: print(s.lower())
else: print(s.upper())
