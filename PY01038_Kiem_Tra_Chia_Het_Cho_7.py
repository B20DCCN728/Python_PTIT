import math
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        tmp = int(input())
        while tmp % 7 != 0:
            tmp += int(str(tmp)[::-1])
        print(tmp)
        t -= 1
