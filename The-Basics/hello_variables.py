"""Variables are pointers to specific values assigned in memory"""

# Create numerical and string variables
name = "Carlos"
greetings = "Hi"

a = 12
b = 3

print(greetings + " " + name)

print("=" * 10)

print(a/b)  # Float division
print(a//b)  # Integer division
print(a % 5)  # Reminder after division

# Python follows operator precedence (/ and *), (+ and -)
print(a + b/3 - 4*12)

print("=" * 10)

# String slicing
my_string = "Look who's taking"
print(my_string)
print(my_string[0])
print(my_string[1])
print(my_string[-1])
print(my_string[0:7])
print(my_string[7:])

print("=" * 10)

# Search in an string with in operator

today = "friday"
print("day" in today)
print("fri" in today)
print("mon" in today)
