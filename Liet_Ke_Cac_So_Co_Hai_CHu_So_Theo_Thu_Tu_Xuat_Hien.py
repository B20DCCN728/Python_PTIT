if __name__ == "__main__":
    solve = input()
    n = len(solve) if len(solve) % 2 == 0 else len(solve) - 1
    res = []
    for i in range(0, n - 1, 2):
        if solve[i:i + 2] not in res:
            res.append(solve[i:i + 2])
    print(" ".join(res))