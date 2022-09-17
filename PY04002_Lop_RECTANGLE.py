class Rectangle:
    def __init__(self, hei, wid, col):
        self.hei = hei
        self.wid = wid
        self.col = col
    
    def perimeter(self):
        return (self.wid + self.hei) * 2

    def area(self):
        return self.hei * self.wid

    def color(self):
        return self.col.title()

    def check(self):
        if self.hei <= 0 or self.wid <= 0: return False
        return True

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.check() == False: print('INVALID')
else: print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
