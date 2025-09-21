marks_list = [95, 67, 32, 88, 40, 23, 76, 59, 39, 100]

def grade(mark):
    if mark >= 40:
        return "Pass"
    else:
        return "Fail"
    
for i in marks_list:
    print(grade(i))