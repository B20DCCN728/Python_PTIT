era = [0] * 1000001

def Era():
    era[0] = era[1] = 1
    for x in range(2, 1000):
        if era[x] == 0:
            for i in range(x * x, 1000001, x):
                era[i] = 1

if __name__ == "__main__":
    t = int(input())
    Era()
    while t > 0:
        count = 0
        n = int(input())
        for i in range(0, n):
            if era[i] == 0 and i + 6 < n:
                if era[i + 2] == 0 and era[i + 6] == 0: count += 1
                if era[i + 4] == 0 and era[i + 6] == 0: count += 1
        print(count)
        t-= 1