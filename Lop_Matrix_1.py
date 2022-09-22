class Matrix:
    def __init__(self, solve, re_solve, n, m):
        self.solve = solve
        self.re_solve = re_solve
        self.n = n
        self.m = m

    def solved(self):
        res = [[0] * self.n for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.solve[i][k] * self.re_solve[k][j]
        return res


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m = [int(x) for x in input().split()]
        data = [[int(j) for j in input().split()] for i in range(n)]
        re_data = [[0] * n for x in range(m)]
        for i in range(n):
            for j in range(m):
                re_data[j][i] = data[i][j]
        s1 = Matrix(data, re_data, n, m)
        res = s1.solved()
        for i in range(n):
            print(*res[i])
        t -= 1

"""
1 3   1 5 2 3
5 9   3 9 4 5
2 4
3 5
"""