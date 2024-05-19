"""
count_chars = {}
{"i":4, "I":1}

str.count(char)  #
"""
detail = "India is a beautiful country to live"
set = set(detail)
print(f"SET is {set}")
print(f"Total items are in the set is {len(set)}")
print(f"Total chars in the str is {len(detail)}")
print(f"Count of i is {detail.count("i")}")
print(f"Count of b is {detail.count("b")}")
print(f"Count of a is {detail.count("a")}")

dict_comp = {item:detail.count(item) for item in detail} # {"I":detail.count("I"), "n":detail.count("n")..................}
print(f"Dict comp is {dict_comp}")

using_set = {item:detail.count(item) for item in set} # {"I":detail.count("I"), "n":detail.count("n")..................}
print(f"Dict comp is {using_set}")

for item in dict_comp.items():
    print(item)
print()
print()
for item in using_set.items():
    print(item)