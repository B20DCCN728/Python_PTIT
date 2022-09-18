import math
Prime = [2, 3, 5, 7]
#
def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
#
def isCheck(solve):
    n = len(solve)
    for i in range(0, n):
        if isPrime(i) == False and int(solve[i]) in Prime: return False
        if isPrime(i) == True and int(solve[i]) not in Prime: return False
    return True
#
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if isCheck(solve): print("YES")
        else: print("NO")
        t -= 1 
