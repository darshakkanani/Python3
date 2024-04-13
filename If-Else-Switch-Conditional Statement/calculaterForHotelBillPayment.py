print("Welcome to the tip calculator")

# Taking input for the total bill
total_bill = float(input("What was the total bill? "))

# Taking input for the number of people
num_people = int(input("How many people to split the bill? "))

# Taking input for the tip percentage
tip_percentage = float(input("What percentage tip would you like to give? (e.g., 10, 20, 30, 40, 50): "))

# Calculating the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Adding tip to the total bill
total_bill += tip_amount

# Calculating the amount each person should pay
amount_per_person = total_bill / num_people

print("Each person should pay: $", round(amount_per_person, 2))
