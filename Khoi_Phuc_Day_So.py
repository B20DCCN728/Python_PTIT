#Created by Campus

if __name__ == "__main__":
    n = int(input())
    solve = []
    if n == 2: print("1 1")   
    else:  
        for i in range(n):
            solve.append([int(x) for x in input().split()])
        res = []
        for i in range(n): res.append(0)
        res[0] = (solve[0][1] + solve[0][2] - solve[1][2]) // 2
        res[1] = solve[0][1] - res[0]
        res[2] = solve[0][2] - res[0]
        for i in range(3, n):
            res[i] = solve[0][i] - res[0]
        print(*res)