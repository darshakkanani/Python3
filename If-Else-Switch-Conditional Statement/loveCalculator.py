name1 = input("Enter the male name: ")
name2 = input("Enter the female name: ")

combined_string = name1 + name2

lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

a = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
b = l+o+v+e

love_score = int(str(a) + str(b))

if love_score > 10 or love_score < 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together") 