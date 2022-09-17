from re import T


def check(sum):
    n = len(sum)
    if n == 1: return False
    for i in range(0, int(n / 2)):
        if(sum[i] != sum[n - i - 1]): return False
    return True

def cal_sum(s):
    n = len(s)
    sum = 0
    for i in range(0, n):
        sum += int(s[i])
    return str(sum)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = input()
        if check(cal_sum(n)) == False: print("NO")
        else: print("YES")
        t -= 1