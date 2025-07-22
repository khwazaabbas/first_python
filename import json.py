import json

# Python to JSON string
data = {"users": [{"id": 1, "name": "Charlie"}, {"id": 2, "name": "Dana"}]}
json_str = json.dumps(data, indent=2)
print("JSON string:")
print(json_str)

# JSON string back to Python
parsed_data = json.loads(json_str)
print("Python object:")
print(parsed_data["users"][0]["name"])  # Output: Charlie

# Write to file
with open('users.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read from file
with open('users.json', 'r') as f:
    loaded_data = json.load(f)
print("From file:")
print(loaded_data)