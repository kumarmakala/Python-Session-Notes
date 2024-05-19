import json

# json.loads()
"""
LOADS converts JSON data to Python DATA
"""

# json.dumps()
"""
DUMPS - Converts PYTHON DATA to JSON DATA
"""

json_data = '{"source":98343493,"name":"John Doe", "message": "Hi Good morning Happy Weekend","dest":4545435}'
python_data = json.loads(json_data)

print(f"Source Person Mob is {python_data["source"]}")
print(f"Source Name is {python_data["name"]}")
print(f"Source Message sent is {python_data["message"]}")

