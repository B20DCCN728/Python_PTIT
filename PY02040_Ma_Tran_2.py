#created by Campus 
if __name__ == "__main__":
    n = int(input())
    solve = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        solve.append(tmp)
    k = int(input())
    count = n - 1
    above = 0
    below = 0
    for i in range(n):
        for j in range(0, count):
            above += solve[i][j]
        for j in range(count + 1, n):
            below += solve[i][j]
        count -= 1
    if abs(above - below) <= k: print("YES")
    else: print("NO")
    print(abs(above - below))
