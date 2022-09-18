from math import gcd


class faction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def _solved(self):
        k = gcd(self.numerator, self.denominator)
        self.numerator //= k
        self.denominator //= k
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    a, b = [int(x) for x in input().split()]
    solve = faction(a, b)
    print(solve._solved())
