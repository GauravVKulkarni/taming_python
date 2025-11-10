# functional programming

def create_role(name, role, rank):
    return {
        'name': name,
        'role': role,
        'rank': rank
    }

def get_name(role_obj):
    return role_obj['name']

def get_role(role_obj):
    return role_obj['role']

def get_rank(role_obj):
    return role_obj['rank']

emp_1 = create_role('Alice', 'Engineer', 5)
emp_2 = create_role('Bob', 'Manager', 7)

print(get_name(emp_1))  # Output: Alice
print(get_role(emp_2))  # Output: Manager
print(get_rank(emp_1))  # Output: 5

# object-oriented programming

class Role:
    def __init__(self, name, role, rank):
        self.name = name
        self.role = role
        self.rank = rank

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_rank(self):
        return self.rank
    
emp_3 = Role('Charlie', 'Designer', 6)
emp_4 = Role('Diana', 'Director', 8)

print(emp_3.get_name())  # Output: Charlie
print(emp_4.get_role())  # Output: Director
print(emp_3.get_rank())  # Output: 6
