#Created by Campus
from re import *

if __name__ == "__main__":
    n = int(input())
    regEx = "[\w\s]+"
    solve = ""
    for i in range(n):
        solve += input() + " "
    solve = solve.lower().strip()
    solve = findall(regEx, solve)
    counter = {}
    for tmp in solve:
        for cnt in tmp.split():
            if cnt in counter: counter[cnt] += 1
            else: counter[cnt] = 1
    for tmp in sorted(counter.items(), key= lambda x: (-x[1], x[0])):
        print(tmp[0], tmp[1])