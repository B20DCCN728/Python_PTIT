t = int(input())
while t > 0:
    number = int(input())
    num_1 = number % 10
    num_2 = 0
    ok = 0
    number //= 10
    while number > 0:
        num_2 = number % 10
        if num_1 < num_2:
            ok = 1
            break
        num_1 = num_2
        number //= 10
    if ok == 0:
        print("YES")
    else: print("NO")
    t -= 1