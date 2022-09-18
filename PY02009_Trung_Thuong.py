if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = {}
        for i in range(0, n):
            tmp = int(input())
            if tmp in solve:
                solve[tmp] += 1
            else: solve[tmp] = 1
        res = 0
        res_value = 0
        for i in solve:
            if res_value == solve[i]:
                if i < res: res = i
            if solve[i] > res_value:
                res_value = max(solve[i], res_value)
                res = i
        print(res)
        t -= 1
        
