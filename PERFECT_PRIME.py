import math
Prime = [2, 3, 5, 7]
#
def isPrime(solve):
    if solve == 1 or solve == 0: return False
    if solve == 2: return True  
    for i in range(2, int(math.sqrt(solve) + 1)):
        if solve % i == 0: return False
    return True
#
class Campus:
    def __init__(self) -> None:
        pass
    def reverse(solve): 
        return int(solve[::-1])
    def sum(solve):
        sum = 0
        for i in solve: sum += int(i)
        return sum
    def isCheck(solve):
        for i in solve:
            if int(i) not in Prime: return False
        return True
#
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = input()
        if isPrime(int(solve)) and isPrime(Campus.reverse(solve)) and isPrime(Campus.sum(solve)) and Campus.isCheck(solve):
            print("Yes")
        else: print("No")
        t -= 1