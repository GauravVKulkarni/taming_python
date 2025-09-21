import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius * radius
        self.circumference = 2 * math.pi * radius