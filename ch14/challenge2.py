class Square:
    square_list = []
    def __init__(self, w):
        self.width = w
        self.square_list.append(self)

    def __repr__(self):
        return (str(self.width) + ' by ') * 3 + str(self.width)

squ = Square(29)
print(squ)
