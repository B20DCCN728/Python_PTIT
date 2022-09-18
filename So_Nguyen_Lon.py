import math
import random

'''
def GCD(a, b):
    if b == 0: return a
    return GCD(b, a % b)
'''

def reduceB(a, b):
    mod = 0
    for i in range(0, len(b)):
        mod = (mod * 10 + int(b[i])) % a
    return mod

def gcdLarge(a, b):
    if a == 0: return b
    return math.gcd(a, reduceB(a, b))

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        a = int(input())
        b = input()
        print(gcdLarge(a, b))
        t -= 1