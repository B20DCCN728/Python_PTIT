import math
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        i = 2
        print("1 ", end = "")
        while i <= math.sqrt(n):
            count = 0
            ok = 1
            while n % i == 0:
                n //= i
                count += 1
                ok = 0
            if ok != 1: print(f"* {i}^{count} ", end = "")
            i += 1
        if n > 1: print(f"* {n}^1", end = "")
        print()
        t -= 1
