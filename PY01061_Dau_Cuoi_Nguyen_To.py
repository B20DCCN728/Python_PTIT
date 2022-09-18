import math

def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        fnum = int(solve[0] + solve[1] + solve[2])
        lnum = int(solve[-3] + solve[-2] + solve[-1])
        if isPrime(fnum) and isPrime(lnum): print("YES")
        else: print("NO")
        t -= 1
