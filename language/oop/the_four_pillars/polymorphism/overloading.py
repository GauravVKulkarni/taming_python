#Overloading not allowed in python
#Here's a worksround

class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, num1, num2):
        return num1 + num2
    
    def add_multiple(self, *args):
        return sum(args)

calcy = Calculator("Calcy")

print(calcy.add_multiple(1,2,3,4,5))
print(calcy.add(1,2))
