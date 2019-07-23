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

print("=" * 10)

# Formatting Strings
age = 25
print("My age was " + str(age) + " ten years ago!")

# Replace fields
print("I am {} year old".format(age))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("=" * 10)

for i in range(1, 12):
    print("No. {0:3} squared is {1:4} and cubed is {2:5}".format(i, i**2, i**3))

print("=" * 10)

print("Pi is approximately {0:12.50}".format(22/7))
