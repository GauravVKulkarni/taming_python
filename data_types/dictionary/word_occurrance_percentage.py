word_counts = {
    "python": 25, "data": 18, "code": 30, "analysis": 12, "ai": 15,
    "model": 10, "learning": 20, "deep": 7, "network": 9, "training": 14,
    "results": 11, "performance": 13, "accuracy": 8
}

word_list = []

total_count = 0

for i in word_counts:
    total_count += word_counts[i]

for i in word_counts:
    word_list.append((i, round(word_counts[i]*100/total_count, 2)))

word_list = dict(sorted(word_list, key=lambda x : x[1], reverse=True)[0:5])

print(word_list)