import math
def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def check(solve):
    res = 0
    n = len(solve)
    for i in range(0, n):
        if (i % 2 == 0 and int(solve[i]) % 2 == 0) or (i % 2 == 1 and int(solve[i]) % 2 == 1): 
            res += int(solve[i])
        else: return False
    if isPrime(res): return True
    else: return False

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if check(solve): print("YES")
        else: print("NO")
        t -= 1