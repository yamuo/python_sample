class Shape:
    def what_am_i(self):
        print("I am a Shape")

class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def calculate_perimeter(self):
        return (self.h + self.w) * 2

class Square(Shape):
    def __init__(self, h):
        self.h = h

    def calculate_perimeter(self):
        return self.h * 4

    def change_size(self,s):
        self.h += s

rectangle = Rectangle(4,8)
print(rectangle.calculate_perimeter())
rectangle.what_am_i()

square = Square(4)
square.change_size(-1)
print(square.calculate_perimeter())
square.what_am_i()

    
