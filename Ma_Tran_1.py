if __name__ == "__main__":
    n = int(input())
    solve = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        solve.append(tmp)
    count = 0
    above = 0
    below = 0
    k = int(input())
    for i in range(n):
        for j in range(0, count):
            below += solve[i][j]
        for j in range(count + 1, n):
            above += solve[i][j]
        count += 1
    if abs(above - below) <= k: 
        print("YES")
    else: print("NO")
    print(abs(above - below))