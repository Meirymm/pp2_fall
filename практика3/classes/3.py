class Shape:
    def area(self,size=0):
        print(size)


class Rectangle(Shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length *self.width
        print(self.area)

s = Shape()
s.area()  # Output: Area of the shape: 0

sq = Rectangle(7,5)
sq.area()  # Output: Area of the shape: 35