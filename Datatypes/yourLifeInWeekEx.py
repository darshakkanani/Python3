a = int(input("Enter your age in year: "))

years_remaining = 90 - a
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"Months: {months_remaining}")
print(f"weeks: {weeks_remaining}")
print(f"days: {days_remaining}")