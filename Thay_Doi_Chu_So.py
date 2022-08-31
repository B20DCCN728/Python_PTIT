import math

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        m, n = [x for x in input().split()]
        p = min(m, n)
        q = max(m, n)
        X_1 = input().strip()
        if " " in X_1: 
            X_1, X_2 = [x for x in X_1.split()]
        else:
            X_2 = input()
        Max = int(X_1.replace(p, q)) + int(X_2.replace(p, q))
        Min = int(X_1.replace(q, p)) + int(X_2.replace(q, p))
        print(f"{Min} {Max}")
        t -= 1