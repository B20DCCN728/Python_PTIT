t = int(input())
while t > 0:
    number = int(input())
    ok = 0
    while number > 0:
        k = number % 10
        if k == 7 or k == 4: 
            number //= 10
            continue
        else: 
            ok = 1
            break
    if ok == 0: print("YES")
    else: print("NO")
    t -= 1