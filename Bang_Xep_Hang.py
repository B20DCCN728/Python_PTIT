#CampusETH
from functools import *
#
class Student:
    def __init__(self, name, problem, submit):
        self.name = name
        self.problem = problem
        self.submit = submit
    def __str__(self) -> str:
        return "{} {} {}".format(self.name, self.problem, self.submit)
#
def cmp_solve(a, b):
    if a.problem < b.problem: return 1
    elif a.problem == b.problem: 
        if a.submit > b.submit: return 1
        elif a.submit == b.submit:
            if a.name > b.name: return 1
        else: return -1
    else: return -1
#
if __name__ == "__main__":
    n = int(input())
    data = []
    while n > 0:
        name = input()
        x, y = [int(z) for z in input().split()]
        data.append(Student(name, x, y))
        n -= 1
    data.sort(key = cmp_to_key(cmp_solve))
    for i in data:
        print(i)

