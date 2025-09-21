flights = [
    ("New York", "London", 5567), ("London", "Paris", 343), ("Paris", "Berlin", 878),
    ("Berlin", "Rome", 1181), ("Rome", "Madrid", 1365), ("Madrid", "New York", 5761),
    ("New York", "Toronto", 551), ("Toronto", "London", 5712)
]

print(min(flights, key= lambda x : x[2]), max(flights, key= lambda x : x[2]))