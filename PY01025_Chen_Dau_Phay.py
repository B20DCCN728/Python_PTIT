if __name__ == "__main__":
    solve = [x for x in input()]
    solve.reverse()
    res = []
    n = len(solve)
    count = 0
    for i in range(0, n):
        count += 1
        res += [solve[i]]
        if count == 3 and i != n - 1:
            res += [',']
            count = 0
    res.reverse()
    for i in range(0, len(res)): print(res[i], end = "")
