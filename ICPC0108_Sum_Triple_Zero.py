if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = sorted([int(x) for x in input().split()])
        count = 0
        for k in range(0, n - 2):
            l = k + 1
            r = n - 1
            while l < r:
                compare = solve[k] + solve[l] + solve[r]
                if compare == 0:
                    count += 1
                    l += 1
                elif compare < 0:
                    l += 1
                else: r -= 1
        print(count) 
        t -= 1
