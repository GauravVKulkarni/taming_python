transactions = [1001, 1002, 1003, 1004, 1001, 1005]

transactions_set = set()
length = 0
duplicates = set()

for i in transactions:
    transactions_set.add(i)
    if length + 1 != len(transactions_set):
        duplicates.add(i)
    else:
        length += 1

print(duplicates)