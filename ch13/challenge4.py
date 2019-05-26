class Horse:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider



class Rider:
    def __init__(self, name):
        self.name = name

mike = Rider("Mike")
stanley = Horse("stanley", "black", mike)

print(stanley.rider.name)
