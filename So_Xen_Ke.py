import math
def check(solve):
    n = len(solve)
    if n % 2 != 1: return False
    if solve[1] == solve[0]: return False
    for i in range(2, n, 2):
        if solve[i] != solve[i - 2]: return False
    return True


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if check(solve): print("YES")
        else: print("NO")
        t -= 1