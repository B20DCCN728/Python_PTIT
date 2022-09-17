#Con 1 cach xai quay lui
res = []
def check(n):
    for i in n:
        if int(i) % 2 == 1: return False
    return True
def creat_res():
    n = 2
    while n <= 988:
        val = str(n)
        if check(val): res.append(int(val + val[::-1]))
        n += 2

if __name__ == "__main__":
    t = int(input())
    creat_res()
    while t > 0:
        n = int(input())
        for i in res:
            if i < n: print(i, end = " ")
        print()
        t -= 1