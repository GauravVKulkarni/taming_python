import json

from field_map import FIELD_MAP

with open("data.json", "r") as f:
    data = json.load(f)

def resolve(data, path):
    for key in path:
        data = data[key]
    return data

flattened = {key: resolve(data, path) for key, path in FIELD_MAP.items()}
options = list(flattened.keys())

while True:
    print("Menu :")
    print(options)

    selected_option = input("Enter the option: ").strip()

    if selected_option in flattened:
        print(flattened[selected_option])
    else:
        print("Invalid option!")