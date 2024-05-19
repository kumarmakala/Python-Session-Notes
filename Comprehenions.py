# List Comprehension
import time
my_list = [10, 20, 30, 40]

# Without List Comprehension

power_list = []

for item in my_list:
    print(f"Current item is {item}")
    time.sleep(2)
    power_list.append(item**2) # 10^2 20^2

print(f"Power list is {power_list}")

# With List comprehension
power_list_comprehension = [item**2  for item in my_list]
print(f"Using List comprehension is {power_list_comprehension}")
