if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]
        A.sort()
        B.sort()
        ok = 1
        for x in range(n):
            if A[x] > B[x]: 
                print("NO")
                ok = 0
                break
        if ok == 1:
            print("YES")
        t -= 1
