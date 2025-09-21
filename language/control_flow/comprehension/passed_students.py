scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}

passed_students = {x : "Pass" for x in scores if scores[x] >= 75}

print(passed_students)