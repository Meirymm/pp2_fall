import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

p1 = Point(2, 3)
p1.show()  # Output: Coordinates of the point: (2, 3)

p1.move(5, 7)
p1.show()  # Output: Coordinates of the point: (5, 7)

p2 = Point(1, 1)
distance = p1.dist(p2)
print("Distance between p1 and p2:", distance)