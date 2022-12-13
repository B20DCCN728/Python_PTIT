#Created by Campus
if __name__ == "__main__":
    n, m, k = [int(x) for x in input().split()]
    res, solve = [], []
    for i in range(n + 1): 
        res.append(0)
        solve.append([])
    for i in range(m):
        x, y = [int(tmp) for tmp in input().split()]
        solve[x].append(y)
        solve[y].append(x)
    p = []
    p.append(k)
    res[k - 1] = 1
    while len(p) > 0:
        tmp = p.pop()
        for i in solve[tmp]:
            if res[i - 1] == 0: 
                res[i - 1] = 1
                p.append(i)
    for i in range(n):
        if res[i] == 0:
            print(i + 1)
    
