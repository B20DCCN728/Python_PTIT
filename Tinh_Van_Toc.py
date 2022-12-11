#Created by Campus
from datetime import datetime

formatTime = f"%H:%M"

class VanToc:
    def __init__(self, name, donVi, end) -> None:
        self.name = name
        self.donVi = donVi
        tmp = self.donVi.split()
        self.code = ""
        for cnt in tmp: self.code += cnt[0]
        tmp = self.name.split()
        for cnt in tmp: self.code += cnt[0]
        self.total = 120 / ((datetime.strptime(end, formatTime) - datetime.strptime("6:00", formatTime)).seconds / 3600)
    
    def __str__(self) -> str:
        return "{} {} {} {} Km/h".format(self.code, self.name, self.donVi, round(self.total))

if __name__ == "__main__":
    listVt = []
    n = int(input())
    for i in range(n):
        name, donVi, end = input(), input(), input().strip()
        listVt.append(VanToc(name, donVi, end))
    listVt.sort(key = lambda x: (-x.total))
    print(*listVt, sep = '\n')

