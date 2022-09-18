import math
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        list_dir = {}
        n = int(input())
        solve = input().split()
        for i in solve:
            if i in list_dir:
                list_dir[i] += 1
            else: list_dir[i] = 1
            res = 0
            ok = 0
        for i in list_dir:
            if list_dir[i] > res:
                res = list_dir[i]
                ok = i
        if res > int(len(solve) / 2): print(ok)
        else: print("NO")
        t -= 1
