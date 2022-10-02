#Created by Campus
class Player:
    time, hour, minute = 0, 0, 0
    def __init__(self, code, name, start, end) -> None:
        self.code = code
        self.name = name
        self.start = start
        self.end = end
        x = self.start.split(":")
        y = self.end.split(":")
        self.time =  int(y[0]) * 60 + int(y[1]) - (int(x[0]) * 60 + int(x[1]))
        self.hour = int(self.time / 60)
        self.minute = self.time - self.hour * 60
    
    def __str__(self) -> str:
        return "{} {} {} gio {} phut".format(self.code, self.name, self.hour, self.minute)


if __name__ == "__main__":
    t, solve = int(input()), []
    while t > 0:
        solve.append(Player(input(), input(), input(), input()))
        t -= 1
    solve = sorted(solve, key = lambda x : (-x.time))
    for i in solve: print(i)
