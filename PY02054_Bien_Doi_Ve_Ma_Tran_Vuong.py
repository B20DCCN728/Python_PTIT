'''if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for i in range(n)]
    res = []
    if n > m:
        k, i = 0, 0
        while True:
            if k == n  - m: break
            if (i + 1) % 2 != 0:
                k += 1
            else: res.append(data[i])
            i += 1
        for j in range(i, n):
            res.append(data[j])
    elif n < m:
        for i in range(n):
            x, k = [], 0
            for j in range(m):
                if (j + 1) % 2 == 0 and k < m - n:
                    k += 1
                else: 
                    x.append(data[i][j])
            res.append(x)
    else: res = data
    for i in range(len(res)):
        for j in range(len(res)):
            print(res[i][j], end = " ")
        print()'''

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append([int(i) for i in input().split()])
    tmp = 0 if n > m else 1
    pos = [i for i in range(tmp, abs(n - m) * 2, 2)]
    for i in range(n):
        if (n > m and i not in pos) or n == m:
            print(*a[i])
        elif n < m:
            for j in range(m):
                if j not in pos:
                    print(a[i][j], end=' ')
            print()
