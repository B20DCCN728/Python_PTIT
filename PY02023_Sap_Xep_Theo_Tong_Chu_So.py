if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = [x for x in input().split()]
        solve = sorted(solve, key = lambda res : (sum(int(x) for x in res), int(res)))
        print(*solve)
        t -= 1
