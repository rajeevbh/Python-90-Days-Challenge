import random

random_int = random.randint(1,10) # Generate a radom number between 1 and 10
print(random_int)

random_float = random.random() # 0.0000000 - 0.9999999
print(random_float)

random_float = random.random() * 5 # Float number between 1 and 4.999
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")

dice_value = random.randint(1,6)
print(f"you got {dice_value} in dice.")