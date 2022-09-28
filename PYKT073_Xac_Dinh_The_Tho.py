if __name__ == "__main__":
    n = int(input())
    res = []
    data = []
    ok = 0
    for i in range(n):
        data.append([x for x in input().split()])
    for i in range(n):
        if len(data[i]) == 6 or len(data[i]) == 8:
            if i == n - 1 or len(data[i + 1]) == 7:
                res.append(1)
        if len(data[i]) == 7: ok += 1
        if ok == 4: 
            res.append(2)
            ok = 0
    print(len(res))
    for i in res:
        print(i)

