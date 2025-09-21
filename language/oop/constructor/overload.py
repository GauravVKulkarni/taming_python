class Rectangle:
    def __init__(self, length, breadth):
        self.length = max(length, breadth)
        self.breadth = min(length, breadth)

    @classmethod
    def from_string(cls, string):
        l, b = map (int, string.split(","))
        return cls(max(l,b), min(l,b))

    def describe(self):
        return {"Length":self.length, "Breadth":self.breadth}

rec1 = Rectangle(10,20)
rec2 = Rectangle.from_string("30,40")

print(rec1.describe())
print(rec2.describe())