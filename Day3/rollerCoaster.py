# Rollercoaster ride bill calculator

print("Welcome to the Rollercoaster")

height = int(input("What is your height(in cm)?: "))

if (height >= 120):
    print("Congrats !!, you are eligible to ride on rollercoaster.")
    age = int(input("what is your age? "))

    if (age <= 12):
        bill = 100
        print(f"Please pay {bill} ruppee for the ride.")
    elif (age <= 18):
        bill = 150
        print(f"Please pay {bill} ruppee for the ride.")
    elif (age >= 45 and age <=55):
        print("Your ride is free of cost")
    else:
        bill = 200
        print(f"Please pay {bill} ruppee for the ride.")

    want_photo = input("Do you want a photo taken (Y / N): ")
    if (want_photo == "Y" or "y"):
        bill = bill + 50
        print(f"Your final bill be {bill}")

else:
    print("Sorry, you have to go taller before you can ride. ")