#Created by Campus
from datetime import datetime 

formatTime_L = "%d/%m/%Y"
formatTime_N = "%H:%M"

class Test:
    def __init__(self, index, codeSubject, subject, day, hour, start) -> None:
        self.code = "T%03d" % index
        self.codeSubject = codeSubject
        self.subject = subject
        self.day = day 
        self.compareDay = (datetime.strptime(self.day, formatTime_L) - datetime.strptime("1/1/2021", formatTime_L)).days
        self.hour = hour
        self.compareHour = (datetime.strptime(self.hour, formatTime_N) - datetime.strptime("06:00", formatTime_N)).seconds // 60
        self.start = start
    
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.code, self.codeSubject, self.subject, self.day, self.hour, self.start)

if __name__ == "__main__":
    listSubject = {}
    n, m = [int(x) for x in input().split()]
    for i in range(n):
        code, name = input(), input()
        listSubject[code] = name
    listTest = []
    for i in range(m):
        codeSubject, day, hour, start = [x for x in input().split()]
        listTest.append(Test(i + 1, codeSubject, listSubject[codeSubject], day, hour, start))
    listTest.sort(key= lambda x: (x.compareDay, x.compareHour, x.codeSubject))
    print(*listTest, sep= '\n')
