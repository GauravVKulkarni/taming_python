class Father():

    prefix = "Mr."

    def __init__(self, name):
        self.name = name

    def describe(self):
        return {"Prefix": self.prefix, "Name": self.name}
    
    def father_function(self):
        return {"Source" : "Father class"}
    
class Mother():
    
    prefix = "Mrs."

    def __init__(self, name):
        self.name = name

    def describe(self):
        return {"Prefix": self.prefix, "Name": self.name}
    
    def mother_function(self):
        return {"Source" : "Mother class"}
    
class Child(Father, Mother):

    def __init__(self,name, prefix):
        super().__init__(name)
        self.prefix = prefix

    def describe(self):
        return {"Prefix": self.prefix, "Name": self.name}

dad = Father("John")
mom = Mother("Jane")
son = Child("Jim", "Mr.")

print(son.describe())
print(son.father_function())
print(son.mother_function())