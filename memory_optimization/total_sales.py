yearly_sales = [
    15000, 22000, 18000, 24000, 30000, 27000, 32000, 29000, 31000, 28000, 26000, 33000
]

total_profitable_sales = sum(sale for sale in yearly_sales if sale > 20000)

print(f"Total Sales : {total_profitable_sales}")