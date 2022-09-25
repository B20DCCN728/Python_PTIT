#CampusETH
class Student:
    def __init__(self, name, dateOfBirth, score1, score2, score3):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.totalScore = self.score1 + self.score2 + self.score3
    def __str__(self) -> str:
        return "{} {} {:.1f}".format(self.name, self.dateOfBirth, self.totalScore)
#
if __name__ == "__main__":
    solve = Student(input(), input(), float(input()), float(input()), float(input()))
    print(solve)
