def generate_numbers():
    """A unnecessarily complicated generator that yields numbers from 0 to 20."""
    yield 0
    for number in range(1, 6):
        yield number
    yield 6
    for number in range(7, 11):
        yield number
    yield 11
    for number in range(12, 16):
        yield number
    yield 16
    for number in range(17, 21):
        yield number

numbers = generate_numbers()

print(numbers)

print(next(numbers))
print(next(numbers))

for num in numbers:
    print(num)

# This won't work.
print(next(numbers))