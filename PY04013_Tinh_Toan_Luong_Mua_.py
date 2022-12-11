#Created by Campus
import math
from datetime import datetime
from collections import defaultdict
if __name__ == "__main__":
    n = int(input())
    listRain = defaultdict(list)
    index = 1
    for i in range(n):
        city, start, end, rainAmount = input(), input(), input(), int(input())
        formatTime = f"%H:%M"
        totalRainTime = (datetime.strptime(end, formatTime) - datetime.strptime(start, formatTime)).seconds // 60
        if city in listRain.keys():
            listRain[city][1] += rainAmount
            listRain[city][2] += totalRainTime
        else: 
            listRain[city] = ["T%02d" % index, rainAmount, totalRainTime]
            index += 1
    for city in listRain.keys():
        print("{} {} {:.2f}".format(listRain[city][0], city, listRain[city][1] / listRain[city][2] * 60))
