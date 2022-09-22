import math
#
def isPrime(solve):
    if solve == 1 or solve == 0: return False
    if solve == 2: return True  
    for i in range(2, int(math.sqrt(solve) + 1)):
        if solve % i == 0: return False
    return True
#
if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    a = set()
    solve = []
    for i in range(n):
        b = [int(x) for x in input().split()]
        solve.append(b)
        b = set(b)
        a = a.union(b)
    a = list(a)
    a.sort(reverse = True)
    k = 0
    for i in a:
        if isPrime(i):
            k = i
            break
    if k == 0: print("NOT FOUND")
    else:
        print(k)
        for i in range(n):
            for j in range(m):
                if solve[i][j] == k:
                    print(f"Vi tri [{i}][{j}]")

