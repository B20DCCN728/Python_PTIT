if __name__ == "__main__":
    solve = input()
    n = len(solve)
    res = []
    if n % 2 != 0: n -= 1
    for i in range(0, n, 2):
        res.append(int(solve[i:i + 2]))
    a = {}
    for i in res:
        if i in a:
            a[i] += 1
        else: a[i] = 1
    for i in a:
        print(f"{i} {a[i]}")