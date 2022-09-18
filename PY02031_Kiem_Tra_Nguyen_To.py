import math
def isPrime(n):
    if n == 1 or n == 0: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    arr = [] * n 
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        for j in range(m):
            if isPrime(tmp[j]): tmp[j] = 1
            else: tmp[j] = 0 
        arr.append(tmp)
    for i in range(n):
        for j in range(m): print(arr[i][j], end = " ")
        print()
