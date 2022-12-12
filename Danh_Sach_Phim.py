#Created by Campus
from datetime import datetime
from collections import defaultdict

formatTime = "%d/%m/%Y"

class Movie:
    def __init__(self, index, topic, start, name, amount) -> None:
        self.code = "P%03d" % index
        self.topic = topic
        tmp = datetime.strptime(start, formatTime)
        self.start = (tmp - datetime.strptime("1/1/2021", formatTime)).days
        self.time = tmp.strftime(formatTime)
        self.name = name
        self.amount = amount
    
    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.code, self.topic, self.time, self.name, self.amount)

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    listTopic = {}
    for i in range(n):
        code, topic = "TL%03d" % (i + 1), input()
        listTopic[code] = topic
    listMovie = []
    for i in range(m):
        code, start, name, amount = input(), input(), input(), int(input())
        listMovie.append(Movie(i + 1, listTopic[code], start, name, amount))
    listMovie.sort(key= lambda x: (x.start, x.name, -x.amount))
    print(*listMovie, sep= '\n')
    