import random

z = random.randint(1,3)
a = int(input("What do you choose?\n1 => Rock\n2 => Paper\n3 => Scissors\n"))

if a <= 3 and a >= 1:
    if a == 1 and z == 3:
        print(f"Computer: {z}")
        print(f"You: {a}")
        print("Win")
    elif a == 2 and z == 1:
        print(f"Computer: {z}")
        print(f"You: {a}")
        print("Win")
    elif a == 3 and z == 2:
        print(f"Computer: {z}")
        print(f"You: {a}")
        print("Win")
    else:
        print(f"Computer: {z}")
        print(f"You: {a}")
        print("Lose")
else:
    print("Wrong Choise")

