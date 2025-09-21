def discount_calculator(discount):
    def calculator(amount):
        return amount - amount*discount
    return calculator


ten_percent = discount_calculator(0.1)
twenty_percent = discount_calculator(0.2)

print(ten_percent(200))
print(twenty_percent(250))