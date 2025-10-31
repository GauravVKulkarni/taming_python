menu_inr = {
    "pizza" : 120,
    "burger" : 80,
    "pasta" : 100,
    "salad" : 70,
    "soda" : 30
}

inr_to_usd = 82.0

menu_usd = {item: round(price / inr_to_usd, 2) for item, price in menu_inr.items()}

print(menu_usd)