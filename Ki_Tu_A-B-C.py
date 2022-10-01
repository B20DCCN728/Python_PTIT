#Created by Campus
b = ['A', 'B', 'C']
data = []
#
def Try(solve, n, x, y, z):
    if len(solve) == n and x > 0 and x <= y and y <= z: print(solve)
    if len(solve) < n:
        Try(solve + 'A', n, x + 1, y, z)
        Try(solve + 'B', n, x, y + 1, z)
        Try(solve + 'C', n, x, y, z + 1)
#
if __name__ == "__main__":
    n = int(input())
    for i in range(3, n + 1):
        Try("", i, 0, 0, 0)