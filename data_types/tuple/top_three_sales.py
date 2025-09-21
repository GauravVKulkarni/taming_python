sales = [
    (201, "Laptop", 120), (202, "Smartphone", 250), (203, "Tablet", 180),
    (204, "Headphones", 300), (205, "Keyboard", 150), (206, "Monitor", 200),
    (207, "Mouse", 270), (208, "Charger", 90), (209, "Camera", 140),
    (210, "Printer", 160)
]

print(sorted(sales, key= lambda x: x[2], reverse= True)[0:3])