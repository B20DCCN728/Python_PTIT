#Created by Campus
import math
from datetime import datetime

formatTime = f"%d/%m/%Y"

class Bills:
    def __init__(self, index, name, roomCode, start, end, fee) -> None:
        self.code = "KH%02d" % index
        self.name = name
        self.roomCode = roomCode
        self.totalDay = (datetime.strptime(end, formatTime) - datetime.strptime(start, formatTime)).days + 1
        self.totalMoney = self.totalDay * self.setPrice() + fee
    
    def setPrice(self) -> int:
        if self.roomCode[0] == '1': return 25
        elif self.roomCode[0] == '2': return 34
        elif self.roomCode[0] == '3': return 50
        else: return 80

    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.code, self.name, self.roomCode, self.totalDay, self.totalMoney)

if __name__ == "__main__":
    listBills = []
    n = int(input())
    for i in range(n):
        name, roomCode, start, end, fee = input(), input(), input().strip(), input().strip(), int(input())
        listBills.append(Bills(i + 1, name, roomCode, start, end, fee))
    listBills.sort(key = lambda x: (-x.totalMoney))
    #for client in listBills:
        #print(client)
    print(*listBills, sep = '\n')
