

# Nested dict means dict has inside dict

person_details = {"name": "John Doe",
                  "address":
                      {"state": "USA",
                       "city":{"local": "XYZ", "central":"NY"}}}

print(f"Line 10 Person name is {person_details["name"]}  Person city is {person_details["address"]["city"]["local"]}")







# Len() - It gives how many items are available
print(f"Total items in the dict is {len(person_details)}")
print(f"Full dict is {person_details}")
print(f"Person name is {person_details["name"]}")
print(f"Address is {person_details["address"]}")
print(f"Address STATE is {person_details["address"]["state"]}")
print(f"Address CITY is {person_details["address"]["city"]}")
print(f"Address CITY LOCAL is {person_details["address"]["city"]["local"]}")
print(f"Address CITY CENTRAL is {person_details["address"]["city"]["central"]}")