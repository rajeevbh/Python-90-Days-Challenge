# Program to illustrate multiple conditions using logical operator

print("Welcome to the Love Calculator")

name1 = input("What is your name: \n")
name2 = input("What is their name: \n")

combined_name = name1 + name2

name_lowecase = combined_name.lower()

# Counting true
t = name_lowecase.count("t")
r = name_lowecase.count("r")
u = name_lowecase.count("u")
e = name_lowecase.count("e")

true = t + r + u + e

l = name_lowecase.count("l")
o = name_lowecase.count("o")
v = name_lowecase.count("v")
e = name_lowecase.count("e")

love = l + o + v + e

love_score = str(true) + str (love) # Coverting into string because we have concatenate digit
love_score = int(love_score)

if (love_score < 10) or (love_score < 90):
    print(f"Your love score is {love_score}. You should go and spend some time together")
elif (love_score >= 40 ) and (love_score <= 50):
    print(f"Your love score is {love_score}. You are already together.")
else:
    print(f"Your love score is {love_score}.")