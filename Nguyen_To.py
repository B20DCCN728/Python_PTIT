from cmath import sqrt
import math
from pickle import TRUE


def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a -= b
        else: b -= a
    return a

def check_prime(n):
    if n == 1 or n == 0: return 0
    if n == 2: return 1
    if n % 2 == 0: return 0
    print(int(math.sqrt(n)))
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1


t = int(input())
while t > 0:
    k = 0
    n = int(input())
    for i in range(1, n):
        if gcd(i, n) == 1: k += 1
    if check_prime(k) == 1: print("YES")
    else: print("NO")
    t -= 1