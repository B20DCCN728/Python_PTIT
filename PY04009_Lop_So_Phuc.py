#Created by Campus
class sophuc(complex):
    def __init__(self, x) -> None:
        super().__init__()
    def __str__(self) -> str:
        if "-" in str(self.imag):
            return ('%i - %ii' % (self.real, -self.imag))
        else: 
            return ('%i + %ii' % (self.real, self.imag))
    

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        a, b, c, d = [int(x) for x in input().split()]
        x = sophuc(complex(a, b))
        y = sophuc(complex(c, d))
        xx = sophuc((x + y) * x)
        yy = sophuc((x + y) ** 2)
        print(str(xx) + ', ' + str(yy))
        t -= 1
