def generate_fibonacci():
    num1 = 0
    num2 = 1
    yield num1
    yield num2
    while True:
        yield num1 + num2
        num1, num2 = num2, num1
        num2 = num1 + num2

fibonacci_series = generate_fibonacci()

for i in range (0, 10):
    print(next(fibonacci_series))