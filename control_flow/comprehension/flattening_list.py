matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_list = [x for row in matrix for x in row]

print(flattened_list)