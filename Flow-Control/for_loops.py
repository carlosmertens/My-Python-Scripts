""" For loops """

# for and range - numerical
for i in range(1, 11):
    print("Now, i is: {}".format(i))

print("*" * 10)

for i in range(0, 101):
    if i % 7 == 0:
        print(i)  # Print numbers divisible by 7

print("*" * 10)

# for and range - Strings
my_text = "abcdefg"
for i in range(0, len(my_text)):
    print(my_text[i])

print("*" * 10)

my_str_numbers = "456, 755, 245 and 8655"
for i in range(0, len(my_str_numbers)):
    if my_str_numbers[i] in "0123456789":
        print(my_str_numbers[i], end="")

print("")

# for and in

for char in my_str_numbers:
    if char in "0123456789":
        print(char, end=" ")

print("")

my_list = ["three", "two", "one"]
for item in my_list:
    print("Counting down: " + item)

print("*" * 10)

# Nested for loops
for i in range(1, 5):
    for j in range(1, 11):
        print("{} multiply by {} is: {}".format(j, i, i*j))
    print("=" * 10)

# Exercise

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for i in quote:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i)
