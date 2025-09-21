prices = [
    100, 102, 101, 105, 107, 106, 108, 110, 109, 111,
    115, 113, 116, 118, 120, 119, 121, 123, 122, 125,
    128, 127, 129, 130, 132, 131, 133, 135, 134, 136
]

def generate_rolling_average(prices_list, window_size):
    total = sum(prices_list[0:window_size])
    i = window_size
    yield(round(total/window_size))
    while(i<len(prices_list)):
        total = total - prices_list[i-window_size] + prices_list[i]
        i += 1
        avg = round(total/window_size, 2)
        yield avg

rolling_average = generate_rolling_average(prices, 3)

for i in rolling_average:
    print(i)