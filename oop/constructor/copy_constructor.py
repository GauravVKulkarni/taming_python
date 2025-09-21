class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def copy(cls, other_person):
        return cls(other_person.name, other_person.surname, other_person.age)

    def describe(self):
        return {"Name": self.name, "Surname": self.surname, "Age": self.age}

person1 = Person("John", "Doe", "100")
twin_of_person1 = Person.copy(person1)
twin_of_person1.name = "Jane"

print(person1.describe())
print(twin_of_person1.describe())