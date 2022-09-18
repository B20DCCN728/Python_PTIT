'''
solve = input()
n = len(solve)
visited = [0] * n

def Try(res, k):
    if k == n:
        print(res)
        return 
    for i in range(0, n):
        if visited[i] == 0:
            visited[i] = 1
            Try(res + solve[i], k + 1)
            visited[i] = 0

Try("", 0)
'''
from itertools import permutations  
if __name__ == "__main__":
    solve = input()
    perm = permutations(solve)      
    for i in perm:
        print("".join(i))   
