# class - a template for creating objects with common attributes
# object - an instance of a class with values of its own assigned to the attributes
# constructor - a function that generates an object using the template provided by the class definition and some values for assigning to attributes


class Student:

    university_name = "Prof. Dhoomketu University of Fictional Sciences, Dholakpur"

    def __init__(self, student_id : int, student_name : str, student_age : int):
        self.id = student_id
        self.name = student_name
        self.age = student_age
    
    def describe_student(self):
        return {"ID": self.id, "Name": self.name, "Age": self.age, "University": self.university_name}
    

student1 = Student(1, "Gaurav", 100)

print(student1.describe_student())