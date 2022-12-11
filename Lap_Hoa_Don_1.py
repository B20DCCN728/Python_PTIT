#Created by Campus
import math

class Bills:
    def __init__(self, name, start, end, order) -> None:
        self.code = "KH{:02d}".format(order)
        self.name = name 
        self.count = end - start

    def getTotal(self) -> float:
        if self.count <= 50:
             return (100 * self.count) * 1.02
        elif self.count <= 100: 
            return (100 * 50 + 150 * (self.count - 50)) * 1.03
        else: return (100 * 50 + 150 * 50 + 200 * (self.count - 100)) * 1.05
    
    def __str__(self) -> str:
        return f"{self.code} {self.name} {round(self.getTotal())}"

if __name__ == "__main__":
    listKH = []
    n = int(input())
    for i in range(n):
        listKH.append(Bills(input(), int(input()), int(input()), i + 1))
    listKH.sort(key = lambda x: (-x.getTotal()))
    for x in listKH:
        print(x)