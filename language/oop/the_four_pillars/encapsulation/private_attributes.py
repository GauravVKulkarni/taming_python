class Secretive:
    def __init__(self, name):
        self.name = name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def describe_secretly(self):
        return {"Name" : self.name}
    
    def describe_openly(self):
        return {"Name" : self.name, "Age": self.get_age()}
    
person1 = Secretive("Micheal")
person1.set_age(100)

print(person1.name)

print(person1.describe_secretly())
print(person1.describe_openly())

print(person1._Secretive__age)
print(person1.__age)