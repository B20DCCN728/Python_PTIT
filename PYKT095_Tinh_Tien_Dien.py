#Created by Campus

class TienDien:
    def __init__(self, index, nameNotFormat, type, begin, end) -> None:
        self.code = "KH%02d" % index
        self.name = self.setName(nameNotFormat)
        self.type = type
        self.dinhMuc = self.setDinhMuc()
        self.amount = end - begin
        self.tienTDM = self.setTienTDM()
        self.tienVDM = self.setTienVDM()
        self.vat = self.setVAT()
        self.total = self.tienTDM + self.tienVDM + self.vat
        
    def setName(self, nameNotFormat) -> str:
        tmp = nameNotFormat.lower().strip().split()
        name = ""
        for i in range(len(tmp)):
            name += tmp[i][0].upper() + tmp[i][1:] + " "
        name = name.strip()
        return name

    def setDinhMuc(self) -> int:
        if self.type == 'A': return 100
        elif self.type == 'B': return 500
        else: return 200

    def setTienTDM(self) -> int:
        if self.amount < self.dinhMuc: return self.amount * 450
        else: return self.dinhMuc * 450
    
    def setTienVDM(self):
        if self.amount > self.dinhMuc: return (self.amount - self.dinhMuc) * 1000
        else: return 0

    def setVAT(self):
        if self.amount > self.dinhMuc: return self.tienVDM // 20
        else: return 0

    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.code, self.name, self.tienTDM, self.tienVDM, self.vat, self.total)

if __name__ == "__main__":
    n = int(input())
    listClient = []
    for i in range(n):
        name = input()
        type, begin, end = [x for x in input().split()]
        listClient.append(TienDien(i + 1, name, type, int(begin), int(end)))
    listClient.sort(key= lambda x: (-x.total))
    print(*listClient, sep= '\n')
