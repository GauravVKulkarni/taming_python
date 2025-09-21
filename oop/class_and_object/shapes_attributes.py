class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return self.length*2 + self.breadth*2
    

rec1 = Rectangle(10, 20)

print(rec1.area(), rec1.perimeter())