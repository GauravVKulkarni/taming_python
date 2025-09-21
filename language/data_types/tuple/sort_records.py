students = [
    (101, "Alice", 88), (102, "Bob", 75), (103, "Charlie", 92), (104, "David", 85),
    (105, "Eve", 92), (106, "Frank", 73), (107, "Grace", 88), (108, "Heidi", 95),
    (109, "Ivan", 67), (110, "Judy", 91), (111, "Karl", 85), (112, "Leo", 80),
    (113, "Mallory", 92), (114, "Niaj", 88), (115, "Olivia", 95), (116, "Peggy", 75),
    (117, "Quinn", 67), (118, "Ruth", 81), (119, "Sybil", 85), (120, "Trent", 95),
    (121, "Uma", 88), (122, "Victor", 75), (123, "Walter", 92), (124, "Xavier", 95),
    (125, "Yvonne", 90), (126, "Zara", 91), (127, "Aaron", 73), (128, "Bella", 80),
    (129, "Cody", 85), (130, "Daisy", 92)
]

students= sorted(students, key = lambda x : (-x[2],x[0]))

print(students)