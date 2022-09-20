data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solve(num, base):
    res = []
    while num > 0:
        res.append(data[num % base])
        num //= base
    return "".join(res)[::-1]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = [int(x) for x in input().split()]
        print(solve(n, k))
        t -= 1
