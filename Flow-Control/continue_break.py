""" Continue and Break """

# Use continue statement
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "eggs":
        continue  # Skip eggs
    print("Need to buy " + item)

print("*" * 10)

# Use break statement
for item in shopping_list:
    if item == "spam":
        break  # Break out of the loop
    print("Buy " + item)

print("*" * 10)

# Use else statement with break
meal = ["bacon", "egg", "cheese", "onion", "tomatos"]
alergies = "onion"

for i in meal:
    if i == alergies:
        print("I can not have it!")
        break
else:
    print("I will have it!")

print("*" * 10)

# Exercise
# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if (i > 0) and (i % 11 == 0):
        break

print("*" * 10)

# Print out number that are not divisible by 3 or 5
for i in range(1, 21):
    if (i % 3 == 0) or (i % 5 == 0):
        continue
    print(i)

print("*" * 10)

# Augmented Assignment
number = "9.223.324.654.667.890.78"
clean_number = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        #clean_number = clean_number + number[i]
        clean_number += number[i]  # Augmented Assignment

new_number = int(clean_number)
print("The converted number is {}".format(new_number))
