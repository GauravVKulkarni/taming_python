def generate_even(n):
    x = 0
    while x <= n:
        yield x
        x += 2

even_numbers = generate_even(10)

for n in even_numbers:
    print(n)