hight = int(input("Enter your hight (cm): "))
weight = int(input("Enter your weight (kilogram): "))

bmi = (weight*10000)/(hight*hight)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
