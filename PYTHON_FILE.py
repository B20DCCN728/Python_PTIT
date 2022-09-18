def isCheck(solve):
    n = len(solve)
    if n < 3: return False 
    check = solve[n - 3:n]
    if check != ".py": return False
    n = n - 3
    for i in range(0, n):
        if (solve[i] >= 'a' and solve[i] <= 'z') or solve[i] == "_" or solve[i] == ".": continue
        else: return False
    return True


if __name__ == "__main__":
    solve = input().lower()
    if isCheck(solve): print("yes")
    else: print("no")