#Created by Campus
from math import *
#
class Division:
    def __init__(self) -> None:
        pass

    def isPrime(n) -> bool:
        if n < 2: return False
        if n == 2: return True
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0: return False
        return True       
#
if __name__ == "__main__":
    n = int(input())
    solve = [int(x) for x in input().split()]
    data = []
    for i in range(n):
        if solve[i] not in data:
            data.append(solve[i])
    x = 0
    n = len(data)
    Test = False
    sumOfList = sum(data)
    for i in range(n):
        x += data[i]
        sumOfList -= data[i]
        if Division.isPrime(x) and Division.isPrime(sumOfList):
            print(i)
            Test = True
            break
    if Test == False: print("NOT FOUND")
