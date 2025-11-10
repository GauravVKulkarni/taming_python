class Woman:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age - 5

    @age.setter
    def age(self, new_age):
        if new_age < 20:
            raise ValueError("Age cannot be less than 20")
        else:
            self._age = new_age


lady = Woman("Champa", 30)
print(lady.name)
print(lady.age)

lady.age = 25
print(lady.age)

try:
    lady.age = 15
except ValueError as e:
    print(e)

print(lady._age)
print(lady.age)