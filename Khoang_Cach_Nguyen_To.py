'''era = [0] * 1000001
import math
def Era():
    era[0] = era[1] = 1
    for i in range(2, int(math.sqrt(1000001))):
        if era[i] == 0:
            for j in range(i * i, 1000001, i):
                era[j] = 1

if __name__ == "__main__":
    Era()
    n, x = [int(x) for x in input().split()]
    count = 0
    list_dir = []
    for i in range(2, 1000001):
        if era[i] == 0: 
            list_dir.append(i)
            count += 1
        if count == n: break
    print(x, end = " ")
    for i in list_dir:
        x += i
        print(x, end = " ")
'''

import math
def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    list_dir = []
    list_dir.append(2)
    n, x = [int(s) for s in input().split()]
    count = 1
    i = 3
    while count < n:
        if isPrime(i) == True:
            list_dir.append(i)
            count += 1
        i += 2
    print(x, end = " ")
    for j in list_dir:
        x += j
        print(x, end = " ")

