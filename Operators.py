"""
Operators:
    1. Arithmetic
    2. Comparison
    3. Logical
    4. Assignment
    5. Membership
    6. Identity

SYMBOLS
1. Arithmetic
    + ,-, * ,/ ,%, **
2. Comparison
    ==, != ,>, <, >=, <=
3. Logical
    and, or ,not
4. Assignment
    = ,+=, -=, *=, /=, %=
5. Membership
    in, not in
6. Identity
    is


Arithmetic

+ ,-, * ,/ ,%, **

num1 = 10
num2 = 2
print("10**2 is ", 10 ** 2)
print("10*2 is ", 10 * 2)

2. Comparison
    ==, != ,>, <, >=, <=

print("10==10 ", 10 == 10)
print("10>10 ", 10 > 10)
print("10 >= 10 ", 10 >= 10)



3. Logical
    and, or ,not
    and - Both conditions must be True then only True otherwise False
    or - At least one condition True then only True otherwise False
    not - Negates the condition

# and
print("10>3 and 50<20", 10 > 3 and 50 < 20)
print("10>3 and 50>20", 10 > 3 and 50 > 20)


# or
print("10>3 or 50<20", 10 > 3 or 50 < 20)
print("10>3 or 50>20", 10 > 3 or 50 > 20)
print("10<3 or 50<20", 10 < 3 or 50 < 20)

# not

print("not 3>2 is", not 3 > 2)  # not 3>2  not True => False

print("not 3<2 is", not 3 < 2)


4. Assignment
    = ,+=, -=, *=, /=, %=


a = 10
print("a is ", a)

a += 5  # a = a+5  => 10+5  15

print("a += 5 is ", a)


5. Membership
    in, not in


num_list = [2, 3, 4, 5, 10]
print("5 is available in [2, 3, 4, 5, 10] ? ", 5 in num_list)
print("7 is available in [2, 3, 4, 5, 10] ? ", 7 in num_list)

name = "John Doe"
print("d is available in name ?", "d" in name)
print("D is available in name ?", "D" in name)
print("Joh is available in name ?", "Joh" in name)
print("Jho is available in name ?", "Jho" in name)



6. Identity
    is - Checks the address if both address are same then returns True


a = 10
b = 10
c = 20

# TO check which location of the memory it stored use id function
print("a memory location is ", id(a))
print("b memory location is ", id(b))
print("c memory location is ", id(c))
"""

num1 = 10
num2 = 2
print("10**2 is ", 10 ** 2)
print("10*2 is ", 10 * 2)