""" Test Conditions 
if, else and elif"""

# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Hi, what is your name? ")
age = int(input("How old are you, {}? ".format(name)))

if age >= 18 and age <= 30:
    print("Welcome {} to a wonderful holidays!".format(name))
else:
    print("Sorry {}!. Come back in {} year(s)".format(name, 18 - age))

print("*" * 20)

# Elif statement

if age >= 21:
    print("You can drive alone")
elif age < 16:
    print("You are not allow to drive")
else:
    print("You can drive with supervision")
