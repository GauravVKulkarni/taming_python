def generate_countdown(n):
    while n > 0:
        yield n
        n -= 1

countdown_list = generate_countdown(5)

for num in countdown_list:
    print(num)