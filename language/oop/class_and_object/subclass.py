class Animal:
    zoo_name = "Walchand International Park"

    def __init__(self, name):
        self.name = name

    def describe(self):
        return {"Name" : self.name}
    
class Serpant(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def describe(self):
        return {"Name" : self.name, "Length" : self.length}
    
    def describe_like_parentcls(self):
        return super().describe()
    

horse = Animal("Horse")
rattlesnake = Serpant("Rattlesnake", "4ft")

print(horse.describe())
print(rattlesnake.describe_like_parentcls())
print(rattlesnake.describe())