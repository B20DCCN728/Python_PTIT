if __name__ == "__main__":
    n = int(input())
    while n > 0:
        solve = input()
        res = 1
        for i in range(0, len(solve)):
            if solve[i] == '0': continue
            res *= int(solve[i])
        print(res) 
        n -= 1
