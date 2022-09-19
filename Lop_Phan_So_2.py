from math import *

class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, a):
        self.x = self.x * a.y + a.x * self.y
        self.y = self.y * a.y
        k = gcd(self.x, self.y)
        self.x //= k
        self.y //= k
        return f"{self.x}/{self.y}"

if __name__ == "__main__":
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    a = Fraction(x1, y1)
    b = Fraction(x2, y2)
    print(a.add(b))
