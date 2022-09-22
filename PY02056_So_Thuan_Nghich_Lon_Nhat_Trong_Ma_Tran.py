import math
#
def isReversibleNumber(solve):
    solve = str(solve)
    if len(solve) <= 1: return False
    if int(solve[::-1]) == int(solve): return True
    else: return False
#
if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    a = set()
    solve = []
    for i in range(n):
        b = [int(x) for x in input().split()]
        solve.append(b)
        b = set(b)
        a = a.union(b)
    a = list(a)
    a.sort(reverse = True)
    k = 0
    for i in a:
        if isReversibleNumber(i):
            k = i
            break
    if k == 0: print("NOT FOUND")
    else:
        print(k)
        for i in range(n):
            for j in range(m):
                if solve[i][j] == k:
                    print(f"Vi tri [{i}][{j}]")
