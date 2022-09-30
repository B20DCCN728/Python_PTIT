#Created by Campus
'''if __name__ == "__main__":
    n = int(input())
    data = []
    res = {}
    while len(data) < n:
        titlee = input()
        data.append(titlee)
        res[titlee] = 0
        while True:
            solve = input()
            data.append(solve)
            if solve == "": break
            res[titlee] += 1
            if(len(data) == n): break
    for x in res:
        print(f"{x}: {res[x]}")
'''
if __name__ == "__main__":
    n = int(input())
    data = []    
    for i in range(n):
        a = input()
        if a == "":
            print(f"{data[0]}: {len(data) - 1}")
            data.clear()
        else: 
            data.append(a)
    print(f"{data[0]}: {len(data) - 1}")