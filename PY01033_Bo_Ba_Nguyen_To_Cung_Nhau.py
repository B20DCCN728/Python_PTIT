import math
def gcd(n, m):
    if m == 0: return n
    return gcd(m, n % m)
if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    for x in range(n, m - 2):
        for i in range(x + 1, m):
            if math.gcd(x, i) == 1:
                for j in range(i + 1, m + 1):
                    if math.gcd(j, i) == 1 and math.gcd(j, x) == 1: print(f"({x}, {i}, {j})")
    
