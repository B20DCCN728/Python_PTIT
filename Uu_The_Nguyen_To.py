import math
Prime = [2, 3, 5, 7]
#
def isPrime(solve):
    if solve == 1 or solve == 0: return False
    if solve == 2: return True
    for i in range(2, int(math.sqrt(solve) + 1)):
        if solve % i == 0: return False
    return True
#
def isCheck(solve):
    count = 0
    for x in solve:
        if int(x) in Prime: count += 1
    if count > (len(solve) - count): return True
    else: return False
#
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if isPrime(len(solve)) and isCheck(solve): print("YES")
        else: print("NO")
        t -= 1