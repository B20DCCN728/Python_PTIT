import math
if __name__ == "__main__":
    n = int(input())
    data = [input() for i in range(n)]
    res = 0
    for i in range(n):
        d = 0
        c = 0
        for j in range(n):
            if data[i][j] == 'C':
                d += 1
            if data[j][i] == 'C':
                c += 1
        res += math.comb(d, 2) + math.comb(c, 2)
    print(res)

