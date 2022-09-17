import math
res = []

def check(solve):
    for i in solve:
        if int(i) % 2 != 0: return False
    return True

def Solution():
    n = 2
    while n < 1000:
        tmp = str(n)
        if check(tmp):
            res.append(int(tmp + tmp[::-1]))
        n += 2

if __name__ == "__main__":
    t = int(input())
    Solution()
    while t > 0:
        n = int(input())
        for i in res:
            if i < n: print(i, end = " ")
        print() 
        t -= 1
