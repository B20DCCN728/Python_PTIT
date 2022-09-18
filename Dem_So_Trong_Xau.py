
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input().strip()
        ans = input().strip()
        n = len(solve)
        solve = solve.replace(ans, "")
        re_n = len(solve)
        x = len(ans)
        print(int((n - re_n) / x))
        t -= 1