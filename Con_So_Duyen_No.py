if __name__ == "__main__":
    n = int(input())
    while n > 0:
        solve = input()
        if int(solve[0]) == int(solve[len(solve) - 1]): print("YES")
        else: print("NO")
        n -= 1