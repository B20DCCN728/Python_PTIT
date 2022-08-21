def check(S):
    n = len(S)
    if S[0] != S[1]:
        if n == 2: return True
        else: 
            for i in range(2, n):
                if S[i] != S[i - 2]: return False
            return True
    else: return False


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = str(input())
        if check(n): print("YES")
        else: print("NO")
        t -= 1