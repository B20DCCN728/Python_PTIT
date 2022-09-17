if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = [int(x) for x in input().split()]
        s = []
        for i in range(n):
            while len(s) > 0 and solve[i] >= solve[s[-1]]: s.pop()
            if len(s) == 0: print(i + 1, end = " ")
            else: print(i - s[-1], end = " ")
            s.append(i)
        print()
        t -= 1
