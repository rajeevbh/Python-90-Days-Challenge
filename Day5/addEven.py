# Adding Even numbers upto 100

# First Mthon
total = 0
for num in range(2,101,2):
    total = total + num
print(total)

# Second Method
total = 0
for num in range(1,101):
    if num % 2 == 0:
        total = total + num
print(total)
