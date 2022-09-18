res = [0] * 93

if __name__ == "__main__":
    t = int(input())
    res[1] = res[2] = 1
    for x in range(3, 93):
        res[x] = res[x - 2] + res[x - 1]
    while t > 0:
        n, m = [int(x) for x in input().split()]
        for i in range(n, m + 1):
            print(res[i], end = " ")
        print()
        t -= 1
