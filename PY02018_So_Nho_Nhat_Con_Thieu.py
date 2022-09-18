if __name__ == "__main__":
    n = int(input())
    asw = [int(x) for x in input().split()]
    asw.sort()
    ok = 1
    for i in range(1, n):
        if asw[i] - 1 != asw[i - 1]:
            print(asw[i - 1] + 1)
            ok = 0
            break
    if ok == 1: print(asw[n - 1] + 1)
        
