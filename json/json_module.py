import json

# Open the JSON file for reading: json.load
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Open the JSON file for writing: json.dump
with open('write_data.json', 'w') as file:
    json.dump(data, file)

# work with json strings directly: json.loads
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)

# work with json objects directly: json.dumps
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
json_string = json.dumps(data)
print(json_string)


