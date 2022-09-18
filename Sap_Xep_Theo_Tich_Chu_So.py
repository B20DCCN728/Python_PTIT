def multiply(res):
    Sum = 1
    for i in res: Sum *= int(i)
    return Sum

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = [x for x in input().split()]
        solve = sorted(solve, key = lambda res : (multiply(res), int(res)))
        print(*solve)
        t -= 1