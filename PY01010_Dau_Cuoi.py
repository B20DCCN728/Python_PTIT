import array as arr
from array import *

t = int(input())
while t > 0:
    list_dir = arr.array('i')
    num = int(input())
    while num > 0:
        list_dir.append(num % 10)
        num //= 10
    size_list = len(list_dir)
    if list_dir[0] == list_dir[size_list - 2] and list_dir[1] == list_dir[size_list - 1]:
        print("YES")
    else: print("NO")
    t -= 1
