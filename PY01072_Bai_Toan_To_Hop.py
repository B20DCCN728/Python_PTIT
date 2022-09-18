'''n, k = [int(i) for i in input().split()]
list = sorted(list({int(i) for i in input().split()}))
n = len(list)

def deff(i, l):
    global n, k
    if len(l) == k:
        print(*l)
        return
    for j in range(i, n):
        deff(j+1, l+[list[j]])
        
deff (0, [])'''

from itertools import combinations
if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    solve = [int(x) for x in input().split()]
    solve = sorted(set(solve))
    for i in combinations(solve, k):
        print(*i)
