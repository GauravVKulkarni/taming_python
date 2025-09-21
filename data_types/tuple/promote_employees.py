employees = [
    (201, "Alice", "IT", 60000), (202, "Bob", "HR", 45000), (203, "Charlie", "Finance", 70000),
    (204, "David", "IT", 55000), (205, "Eve", "Marketing", 50000), (206, "Frank", "IT", 75000),
    (207, "Grace", "Finance", 72000), (208, "Heidi", "HR", 47000), (209, "Ivan", "Marketing", 53000),
    (210, "Judy", "IT", 65000)
]
output = []
for i in employees:
    emp_id, name, dept, salary = i
    if dept == "IT":
        salary *= 1.1
    output.append((emp_id, name, dept, int(salary)))
print(output)