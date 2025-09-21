input_list = shopping_list = [
    "milk","eggs","bread","apples","bananas","oranges","milk","grapes","carrots",
    "eggs","onions","tomatoes","bread","yogurt","cheese","spinach","milk","oranges",
    "rice","beans","oil","pasta","sugar","flour","bananas","bread","potatoes",
    "apples","carrots","honey","tea","coffee","eggs","cheese","milk","spinach"
]

output_using_set = list(set(input_list))

output_using_list = []
for element in input_list:
    if element not in output_using_list:
        output_using_list.append(element)


output_using_dict = list(dict.fromkeys(input_list))

output_using_list_and_set = []
element_set = set()

for element in input_list:
    if element not in element_set:
        element_set.add(element)
        output_using_list_and_set.append(element)

print(output_using_set)
print(output_using_list)
print(output_using_dict)
print(output_using_list_and_set)