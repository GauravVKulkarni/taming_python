input_list = tasks = [
    "email","meeting","call","report","email","plan","meeting","call","research","email",
    "report","call","meeting","call","review","plan","email","meeting","presentation","call",
    "email","plan","call","report","meeting","email","review","plan","email","meeting","call"
]

#initializing a dictionary
freq_dict = {}

#print(type(freq_dict))

for element in input_list:
    if element not in freq_dict:
        freq_dict[element] = 1
    else:
        freq_dict[element] += 1


freq_dict = sorted(freq_dict.items(), key= lambda x: x[1], reverse= True)
freq_dict = dict(sorted(freq_dict))
print(freq_dict, type(freq_dict))