import math

class Apple:
    def __init__(self, n, w, t, p):
        self.name = n
        self.weight = w
        self.taste = t
        self.price = p

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        s = 2 * math.pi * self.r
        return s

class Triangle:
    def __init__(self, b,h):
        self.b = b
        self.h = h

    def area(self):
        s = self.b * self.h / 2
        return s

class Hexagon:
    def __init__(self, l):
        self.l = l

    def calculate_perimeter(self):
        s = self.l * 6
        return s

circle = Circle(3)
triangle = Triangle(4,9)
hexagon = Hexagon(4)
print(circle.area())
print(triangle.area())
print(hexagon.calculate_perimeter())
    
