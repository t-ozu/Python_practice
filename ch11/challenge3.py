class Triangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height / 2
tri = Triangle(10, 20)
print(tri.area())
