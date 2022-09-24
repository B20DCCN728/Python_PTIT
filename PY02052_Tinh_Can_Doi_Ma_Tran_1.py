if __name__ == "__main__":
    n = int(input())
    solve = [[int(x) for x in input().split()] for i in range(n)]
    k= int(input())
    r, l = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            r += solve[i][j]
        for j in range(i):
            l += solve[i][j]
    res = abs(r - l)
    if res <= k: print("YES")
    else: print("NO")
    print(res)
