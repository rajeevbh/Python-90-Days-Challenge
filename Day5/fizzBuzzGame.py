# Program should print from 1 to 100
# If number is divisible by 3 then, print Fizz instead of number
# If number is divisible by 5 then, print Buzz instead of number
# If number is divisible by 3 and 5 both then, print FizzBuzz instead of number

for num in range(1,100,1):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)