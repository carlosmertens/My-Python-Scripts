""" Test Conditions """

# If, else statements

name = input("Hi, what is your name? ")
age = int(input("How old are you, {}? ".format(name)))

if age >= 18:
    print("{} is old enogh to buy beers".format(name))
else:
    print("{} can't buy beers. Come back in {} year(s)".format(name, 18 - age))

print("*" * 20)

# Elif statement

if age >= 21:
    print("You can drive alone")
elif age < 16:
    print("You are not allow to drive")
else:
    print("You can drive with supervision")
