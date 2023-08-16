#  BMI Calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

h = float(height)
w = float(weight)

bmi = w/h**2
              
print("Your BMI is ", int(bmi))
