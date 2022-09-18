import math

def isCheck(solve):
    re_solve = solve[::-1]
    n = len(solve)
    for i in range(1, n):
        if abs(ord(solve[i]) - ord(solve[i - 1])) != abs(ord(re_solve[i]) - ord(re_solve[i - 1])):
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if isCheck(solve): print("YES")
        else: print("NO")
        t -= 1