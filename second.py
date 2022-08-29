import json

with open("data.json", "r") as new_file:
    # reading old data
    data = json.load(new_file)
    print(data['Google'])

for (key, value) in data.items():
    print(value['password'])
    print(key)

for f in data:
    print(f)
