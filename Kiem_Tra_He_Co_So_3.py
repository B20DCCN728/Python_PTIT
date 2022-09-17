def solve(s):
    for i in s:
        if i != '0' and i != '1' and i != '2': return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = input()
        if solve(n): print("YES")
        else: print("NO")
        t -= 1