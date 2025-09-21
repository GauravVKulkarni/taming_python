enrollments = [
    ("Alice", "Math"), ("Bob", "Math"), ("Charlie", "Physics"),
    ("Alice", "Physics"), ("David", "Chemistry"), ("Eve", "Math"),
    ("Frank", "Chemistry"), ("Alice", "Math"), ("Charlie", "Math"),
    ("Eve", "Physics"), ("Bob", "Chemistry"), ("Grace", "Physics"),
    ("Heidi", "Math"), ("Ivan", "Chemistry"), ("Judy", "Math"),
    ("Mallory", "Physics"), ("Niaj", "Chemistry"), ("Olivia", "Math")
]

course_batches = dict()

for student, course in enrollments:
    if course not in course_batches:
        course_batches[course] = [student]
    elif student not in course_batches[course]:
        course_batches[course].append(student)

print(course_batches)