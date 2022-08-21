def isCoPrime(a, b):
    if a == 0 or b == 0: return a + b
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a
def Reverse(n):
    res = 0
    while n > 0:
        res = (res * 10) + (n % 10)
        n //= 10
    return res

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        if isCoPrime(n, Reverse(n)) == 1: print("YES")
        else: print("NO")
        t -= 1