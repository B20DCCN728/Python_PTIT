from operator import truediv


if __name__ == "__main__":
    n = int(input())
    data = []
    while len(data) < n:
        data.extend([int(x) for x in input().split()])
    k = max(data)
    ok = True
    for i in range(1, k + 1):
        if i not in data:
            print(i)
            ok = False
    if ok == True: print("Excellent!")