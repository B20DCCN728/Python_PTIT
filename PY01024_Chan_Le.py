t = int(input())
while t > 0:
    number = int(input())
    res = 0
    num_1 = number % 10
    num_2 = 0
    ok = 0
    res += number % 10
    number //= 10
    while number > 0:
        num_2 = number % 10
        if abs(num_2 - num_1) != 2:
            ok = 1
            break
        num_1 = num_2
        res += number % 10
        number //= 10
    if ok == 0 and res % 10 == 0:
        print("YES")
    else: print("NO")
    t -= 1
