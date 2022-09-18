import math

if __name__ == "__main__":
    n = int(input())
    solve = [int(x) for x in input().split()]
    length = len(solve)
    res = 0
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if solve[i] > solve[j]: res += 1
    print(res)
