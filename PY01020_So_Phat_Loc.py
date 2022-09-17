t = int(input())

while t > 0:
    number = int(input())
    num_1 = number % 10
    number //= 10
    num_2 = number % 10
    if num_1 == 6 and num_2 == 8: print("YES")
    else: print("NO")
    t -= 1
