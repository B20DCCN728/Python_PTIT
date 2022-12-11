#Created by Campus
id = 0
class Employee:
    code = ""
    score = 0
    def __init__(self, name, lt, th):
        self.name = name
        self.lt = lt
        self.th = th
        global id 
        id += 1
        self.code = "TS0" + "{}".format(id)
        self.score = (self.lt + self.th) / 2
        if self.score < 5: self.status = "TRUOT"
        elif self.score < 8: self.status = "CAN NHAC"
        elif self.score < 9.5: self.status = "DAT"
        else: self.status = "XUAT SAC" 

    def __str__(self) -> str:
        return "{} {} {:.2f} {}".format(self.code, self.name, self.score, self.status)

if __name__ == "__main__":
    t = int(input())
    solve = []
    while t > 0:
        name = input()
        p1 = float(input())
        p2 = float(input())
        if p1 > 10: p1 = p1 / 10
        if p2 > 10: p2 = p2 / 10
        solve.append(Employee(name, p1, p2))
        t -= 1
    solve.sort(key = lambda x: x.score, reverse = True)
    for i in solve:
        print(i)
