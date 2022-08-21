import math
def LCM(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

def checkSum(n):
    count = 0
    while n > 0:
        count += n % 10
        n //= 10
    return count

def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        _input = str(input())
        a, b = _input.split()
        a = int(a)
        b = int(b)
        if isPrime(checkSum(LCM(a, b))): print("YES")
        else: print("NO")
        t -= 1