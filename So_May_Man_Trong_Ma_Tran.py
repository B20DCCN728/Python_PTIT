if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for i in range(n)]
    a, b = 0, 10001
    for i in range(n):
        c = max(data[i])
        d = min(data[i])
        if a < c: a = c
        if b > d: b = d
    k = a - b
    ok = False
    d = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == k: 
                d += 1
                if d == 1: print(k)
                print("Vi tri [{}][{}]".format(i, j))
                ok = True
    if ok == False: print("NOT FOUND")

