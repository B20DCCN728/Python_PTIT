#Created by Campus
import math
from datetime import datetime
from collections import defaultdict
class Attendance:
    def __init__(self, code, name, group) -> None:
        self.code = code
        self.name = name
        self.group = group
    
    def setStatus(self, time) -> str:
        point = 10
        for cnt in time:
            if cnt == 'v': point -= 2
            elif cnt == 'm': point -= 1
            else: pass
        if point <= 0: self.status = "0 KDDK"
        else: self.status = f"{point}"

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.code, self.name, self.group, self.status)
        
if __name__ == "__main__":
    n = int(input())
    listSV = {}
    for i in range(n):
        code, name, group = input(), input(), input()
        listSV[code] = Attendance(code, name, group)
    for i in range(n):
        code, time = [x for x in input().split()]
        listSV[code].setStatus(time)
    for code in listSV.keys():
        print(listSV[code])
