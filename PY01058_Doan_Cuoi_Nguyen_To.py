import math
def isPrime(solve):
    if solve == 1 or solve == 0: return False
    if solve == 2: return True
    for i in range(2, int(math.sqrt(solve) + 1)):
        if solve % i == 0: return False
    return True
#
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        n = len(solve)
        solve = int(solve[n - 4:n:])
        if isPrime(solve): print("YES")
        else: print("NO")
        t -= 1
