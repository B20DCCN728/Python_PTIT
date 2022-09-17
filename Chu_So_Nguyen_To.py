import math
def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
def solved(solve):
    n = len(solve)
    if isPrime(n): 
        x = 0
        y = 0
        for i in solve:
            if(i == '2' or i == '3' or i == '5' or i == '7'): x += 1
            else: y += 1
        if x > y: return True
        else: return False
    else: return False

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if solved(solve): print("YES")
        else: print("NO")
        t -= 1