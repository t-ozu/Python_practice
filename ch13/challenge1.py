class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2


class Square:
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

rect = Rectangle(50,30)
squ = Square(50)

print(rect.calculate_perimeter())
print(squ.calculate_perimeter())
