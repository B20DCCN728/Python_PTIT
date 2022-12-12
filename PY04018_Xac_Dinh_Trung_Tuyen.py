#Created by Campus
class Teacher:
    def __init__(self, index, name, maXt, p1, p2) -> None:
        self.code = "GV%02d" % index
        self.name = name
        self.maXt = maXt
        self.bonus = self.setBonus()
        self.subject = self.setSubject()
        self.point = p1 * 2 + p2 + self.bonus
        if self.point >= 18: self.status = "TRUNG TUYEN"
        else: self.status = "LOAI"
    
    def setBonus(self) -> float:
        cmp = self.maXt[1:]
        if cmp == "1": return 2.0
        elif cmp == "2": return 1.5
        elif cmp == "3": return 1.0
        else: return 0.0

    def setSubject(self) -> str:
        cmp = self.maXt[0:1]
        if cmp == "A": return "TOAN"
        elif cmp == "B": return "LY"
        else: return "HOA"
    
    def __str__(self) -> str:
        return "{} {} {} {:.1f} {}".format(self.code, self.name, self.subject, self.point, self.status)



if __name__ == "__main__":
    listGV = []
    n = int(input())
    for i in range(n):
        name, maXt, p1, p2 = input(), input(), float(input()), float(input())
        listGV.append(Teacher(i + 1, name, maXt, p1, p2))
    listGV.sort(key= lambda x: (-x.point))
    print(*listGV, sep= '\n')
