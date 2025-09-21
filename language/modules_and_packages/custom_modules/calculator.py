def add(*args):
    return sum(args)

def subtract(num1, num2):
    return num1 - num2

def multiply(*args):
    op = 1
    for i in args:
        op *= i
    return op

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else: return None