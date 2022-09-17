if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = sorted(input())
        count = 0
        while solve[0] >= '0' and solve[0] <= '9':
            count += int(solve[0])
            solve.pop(0)
        res = ''.join(solve) + str(count)
        print(res)
        t -= 1
