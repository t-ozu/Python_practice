class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2


class Square(Shape):
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, w):
        self.width -= w

rect = Rectangle(50,30)
squ = Square(50)

print(rect.what_am_i())
print(squ.what_am_i())

squ.change_size(10)
print(rect.calculate_perimeter())
print(squ.calculate_perimeter())
