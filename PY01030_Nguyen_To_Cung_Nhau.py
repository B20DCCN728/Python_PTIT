import math
def iscoPrime(a, b): #lower than math.gcd
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    a = 10 ** (k - 1)
    b = 10 ** k 
    count = 0
    for i in range(a, b):
        if math.gcd(n, i) == 1: 
            print(i, end = " ")
            count += 1
            if count % 10 == 0: print()
