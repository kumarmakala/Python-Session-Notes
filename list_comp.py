my_list = [10, 20, 30, 40, 45, 90, 45, 17, 13]

even_list = [item for item in my_list if item%2==0]
odd_list = [item for item in my_list if item%2!=0]

print(f"Original list {my_list}")
print(f"Even list {even_list}")
print(f"ODD list {odd_list}")
