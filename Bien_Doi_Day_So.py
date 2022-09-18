import math
def check(solve):
    if solve[0] == solve[1] and solve[1] == solve[2] and solve[2] == solve[3]: return False
    return True

if __name__ == "__main__":
    while True:
        solve = [int(x) for x in input().split()]
        if check(solve) == False and solve[0] == 0: break
        n = len(solve)
        count = 0
        while check(solve):
            count += 1
            tmp = solve[0]
            solve[0] = abs(solve[0] - solve[1])
            solve[1] = abs(solve[1] - solve[2])
            solve[2] = abs(solve[2] - solve[3])
            solve[3] = abs(solve[3] - tmp)
        print(count)