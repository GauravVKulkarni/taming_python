class Employee:
    def __init__(self, emp_id):
        self.id = emp_id

    def salary(self):
        return {"Salary": "12LPA"}
    
class Manager(Employee):
    def __init__(self, emp_id):
        super().__init__(emp_id)

    def salary(self):
        return {"Salary": "20LPA"}
    
emp1 = Employee(1)
mngr1 = Manager(1)

print(emp1.salary())
print(mngr1.salary())