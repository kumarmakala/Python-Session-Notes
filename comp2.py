my_list = [10, 20, 30, 40, 45, 90, 45, 17, 13, [34,56], "India", "US"]

str_list = [item for item in my_list if type(item)==str]

print(f"Original list {my_list}")
print(f"STR list {str_list}")



