from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
def make_speak(animal : Animal):
    return animal.speak()

dalmatian = Dog()
bengal = Cat()

print(make_speak(dalmatian))
print(make_speak(bengal))