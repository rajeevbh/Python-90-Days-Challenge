# Working with list

import random

names_string = input("Enter few names of persons, separated by commas: \n")
names = names_string.split(",")

print(names)
print(names[0]) # First Name

# To get total number of names in the list
count = len(names)
print(count-1)  # Last Name
random_choice = random.randint(0,count-1)
print(names[random_choice] + " is going to pay the bill today for our dinner")