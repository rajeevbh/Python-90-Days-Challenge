# Pizza Order program to illustrate Logical Operator

print("Welcome to the Pizza Deliveries!!")

size = input("What size of Pizza do you want? S, M or L")
herb_dip = input("Do you need herb deep? (Y or N)")
extra_cheese = input("Do you want extra cheese? (Y or N)")

if (size == "S"):
    bill = 200
elif (size == "M"):
    bill = 400
elif (size == "L"):
    bill = 600

if (herb_dip == "Y"):
    bill = bill + 50
if (extra_cheese == "Y"):
    bill = bill + 100

print(f"Your final bill is : {bill} ruppees")
