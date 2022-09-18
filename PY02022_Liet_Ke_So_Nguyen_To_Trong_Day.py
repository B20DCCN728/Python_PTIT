'''
1
era = [0] * 1000001

def Era():
    era[0] = era[1] = 1
    for x in range(2, 1000):
        if era[x] == 0:
            for i in range(x * x, 1000001, x):
                era[i] = 1

if __name__ == "__main__":
    Era()
    n = int(input())
    arr = [int(x) for x in input().split()]
    res = []
    for x in arr:
        if res.count(x) == 0 and era[x] == 0:
            res.append(x)
    for x in res:
        print(x, arr.count(x))    
'''
#2
import math
from re import L
def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    res = {}
    n = int(input())
    arr = [int(x) for x in input().split()]
    for x in arr:
        if isPrime(x):
            if x in res:
                res[x] += 1
            else: res[x] = 1
    for x in res:
        print(x, res[x])
    
    
