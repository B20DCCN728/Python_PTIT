if __name__ == "__main__":
    S = str(input())
    a, k, n = S.split()
    a = int(a)
    k = int(k)
    n = int(n)
    ok = 1
    for i in range(1, 1000000):
        if k * i <= n: break
        if k * i > a:
            print(k * i - a, end=" ")
            ok = 0
    if ok == 1: print(-1)
        