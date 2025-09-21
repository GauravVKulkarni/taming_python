sales = [
    ("Laptop", "Alice", 1200), ("Phone", "Bob", 800), ("Tablet", "Alice", 400),
    ("Laptop", "Charlie", 1150), ("Phone", "David", 750), ("Tablet", "Bob", 450),
    ("Laptop", "Eve", 1250), ("Phone", "Alice", 780), ("Tablet", "Charlie", 420),
    ("Laptop", "Bob", 1190), ("Phone", "Eve", 770), ("Tablet", "David", 460)
]

products_dict = dict()

for product, customer, price in sales:
    if product not in products_dict:
        products_dict[product] = [price, 1]
    else:
        products_dict[product][0] += price
        products_dict[product][1] += 1
print(products_dict)

for i in products_dict:
    total, count = products_dict.get(i)
    products_dict[i] = round(total/count, 2)

print(products_dict)