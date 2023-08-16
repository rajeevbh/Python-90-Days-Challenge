print("Welcome to the Tip Calculator")

bill = float(input("Enter the total Bill amount in rupee: "))
tip = int(input("How much tip would uou liker to give (5, 10, 15, 20): "))
people = int(input("How many persons are there?"))

final_bill = bill + tip
bill_per_persion = final_bill / people
final_amount = round(bill_per_persion,2)

print(f"Each person should pay: {final_amount} ruppees.")

final_amount = "{:.2f}".format(bill_per_persion)

print(f"Each person should pay: {final_amount} ruppees")


