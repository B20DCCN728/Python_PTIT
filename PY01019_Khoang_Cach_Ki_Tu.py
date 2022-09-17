def isTrue(solve):
    re_solve = ""
    for i in solve: re_solve  = i + re_solve
    for i in range(1, len(solve)): 
        if abs(ord(solve[i]) - ord(solve[i - 1])) != abs(ord(re_solve[i]) - ord(re_solve[i - 1])): return False
    return True


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = str(input())
        if not isTrue(solve): print("NO")
        else: print("YES")
        t -= 1
