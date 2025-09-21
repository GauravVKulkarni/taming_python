reviews = [
    ("Inception", "Alice", 5), ("Inception", "Bob", 4), ("Inception", "Charlie", 5),
    ("Interstellar", "Alice", 4), ("Interstellar", "Bob", 5), ("Interstellar", "David", 4),
    ("Dunkirk", "Charlie", 3), ("Dunkirk", "Eve", 4), ("Dunkirk", "Frank", 3),
    ("Tenet", "Alice", 2), ("Tenet", "Bob", 3), ("Tenet", "Charlie", 2),
    ("Memento", "David", 5), ("Memento", "Eve", 5), ("Memento", "Frank", 4),
    ("Prestige", "Alice", 5), ("Prestige", "Charlie", 5), ("Prestige", "Eve", 4)
]

avg_reviews = dict()

for i in reviews:
    if i[0] not in avg_reviews:
        avg_reviews[i[0]] = [0,0]
    avg_reviews[i[0]][0] += i[2]
    avg_reviews[i[0]][1] += 1

for i in avg_reviews:
    total, freq = avg_reviews[i]
    avg_reviews[i].append(round(total/freq, 2))

print(avg_reviews)