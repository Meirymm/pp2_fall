class Shape:
    def area(self,size=0):
        print(size)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        self.area = self.length ** 2
        print(self.area)

s = Shape()
s.area()  # Output: Area of the shape: 0

sq = Square(7)
sq.area()  # Output: Area of the shape: 25