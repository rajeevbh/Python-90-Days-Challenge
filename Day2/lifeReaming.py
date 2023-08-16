# F-String contains expression inside braces

age = input("Enter your age in years: ")

age_int = int(age)

years_remaining = 100-age_int

months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days"
print(message)