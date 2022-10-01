#Created by Campus
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, p = [int(x) for x in input().split()]
        i, count = 1, 0
        while p * i <= n:
            temp = p * i
            while temp % p == 0:
                count += 1
                temp //= p
            i += 1
        print(count)
        t -= 1
