def check(a, b):
    if b == 0: return a
    return check(b, a % b)
if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if check(arr[i], arr[j]) == 1: print(arr[i], arr[j])
    