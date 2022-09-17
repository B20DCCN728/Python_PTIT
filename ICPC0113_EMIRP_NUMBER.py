import math

res = [0] * 1000001

def Era():
    res[0] = res[1] = 1
    for x in range(2, 1000):
        if res[x] == 0:
            for i in range(x * x, 1000001, x): res[i] = 1

if __name__ == "__main__":
    Era()
    t = int(input())
    while t > 0:
        n = int(input())
        for solve in range(1, n):
            tmp = str(solve)
            re_solve = int(tmp[::-1])
            if re_solve > solve and re_solve < n and res[re_solve] == 0 and res[solve] == 0:
                print(f"{solve} {re_solve}", end = " ")
        print()
        t -= 1
