h = int(input("Enter your height in cm: "))
z = 0
if h > 120:
    print("You can ride!")
    a = int(input("Enter your age: "))
    if a < 12 and a < 0:
        z = 5
        a = input("Do you want photos")
        if a == 'yes':
            z = z + 3
            print(f"Pay ${z}")
        elif a == 'no':
            print(f"Pay ${z}")
        else:
            print("Invalid input")

    elif a < 18 and a >= 12:
        z = 7
        a = input("Do you want photos: ")
        if a == 'yes':
            z = z + 3
            print(f"Pay ${z}")
        elif a == 'no':
            print(f"Pay ${z}")
        else:
            print("Invalid input")

    elif a < 100 and a >= 18:
        z = 12
        a = input("Do you want photos: ")
        if a == 'yes':
            z = z + 3
            print(f"Pay ${z}")
        elif a == 'no':
            print(f"Pay ${z}")
        else:
            print("Invalid input")
    else:
        print("Invalid input")

else:
    print("You can't ride")
