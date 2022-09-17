import math
def isCheck(solve):
    if len(solve) < 3: return False
    if solve[1] <= solve[0]: return False
    for i in range(2, len(solve)):
        if solve[i] < solve[i - 1]:
            for j in range(i, len(solve)):
                if solve[j] >= solve[j - 1]:
                    return False
            return True
        if solve[i] == solve[i - 1]: return False 
    return False
        
#
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if isCheck(str(solve)): print("YES")
        else: print(f"NO")
        t -= 1