if __name__ == "__main__":
    solve = input()
    k = int(input())
    data = {}
    n = len(solve)
    if n % 2 != 0: n = n - 1
    for i in range(0, n - 1, 2):
        if solve[i:i + 2] in data:
            data[solve[i:i + 2]] += 1
        else: data[solve[i:i + 2]] = 1    
    ok = False
    for i in sorted(data.keys()):
        if data[i] >= k: 
            print("{} {}".format(i, data[i]))
            ok = True
    if ok == False: print("NOT FOUND")
