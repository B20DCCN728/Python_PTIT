def Solve(solve):
    n = len(solve)
    sum = 0
    pro = 1
    ok = 0
    for i in range(0, n):
        if i % 2 == 0: sum += int(solve[i])
        else:
            if solve[i] == '0': continue
            else:
                ok = 1
                pro *= int(solve[i])
    if ok == 1: return sum, pro
    else: return sum, 0

#Solution
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        sum, pro = Solve(solve)
        print(f"{sum} {pro}")
        t -= 1
