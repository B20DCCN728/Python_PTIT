def fac(n):
    if(n == 0): return 1
    if n == 1: return n
    return n * fac(n - 1)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = int(input())
        n = str(solve)
        res = 0
        for i in range(0, len(n)):
            res += fac(int(n[i]))
        if res == solve: print("Yes")
        else: print("No")
        t -= 1