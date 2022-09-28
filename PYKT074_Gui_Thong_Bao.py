#CampusETH
#Cach 1
'''if __name__ == "__main__":
    t = int(input())
    while t > 0: 
        solve = input()
        n = len(solve)
        if n <= 100: print(solve)
        else: 
            if solve[100] == " ":
                solve = solve[0:99]
                print(solve)
            else:
                ok = 0
                for i in range(99, 0, -1):
                    if solve[i] == " ":
                        ok = i
                        break
                solve = solve[0:ok]
                print(solve)
        t -= 1'''


import textwrap
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        shortened = textwrap.shorten(input(), width = 100, placeholder = "")
        print(shortened)
        t -= 1
