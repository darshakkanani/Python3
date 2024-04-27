print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
print("Extra cheese for any size pizza: + $1")

p = input("Enter pizza's size (S/M/L): ")
z = 0
c = 1
pl = 3
ps = 2
if p == 'S':
    z = 15
    print(f"Pay ${z}")
    print("Do you want to add Pepperoni? ")
    pp = input("Y/N: ")
    print("Do you want to add extra cheese? ")
    pc = input("Y/N: ")
    if pp == 'Y' and pc == 'Y':
        z = z + ps + c
        print(f"Pay ${z}")
    elif pp == 'Y' and pc == 'N':
        z = z + ps
        print(f"Pay ${z}")
    elif pp == 'N' and pc == 'Y':
        z = z + c
        print(f"Pay ${z}")
    elif pp == 'N' and pc == 'N':
        print(f"Pay ${z}") 
    else:
        print("Invalid Input")
elif p == 'M':
    z = 20
    print(f"Pay ${z}")
    print("Do you want to add Pepperoni? ")
    pp = input("Y/N: ")
    print("Do you want to add extra cheese? ")
    pc = input("Y/N: ")
    if pp == 'Y' and pc == 'Y':
        z = z + pl + c
        print(f"Pay ${z}")
    elif pp == 'Y' and pc == 'N':
        z = z + pl
        print(f"Pay ${z}")
    elif pp == 'N' and pc == 'Y':
        z = z + c
        print(f"Pay ${z}")
    elif pp == 'N' and pc == 'N':
        print(f"Pay ${z}") 
    else:
        print("Invalid Input")
elif p == 'L':
    z = 25
    print(f"Pay ${z}")
    print("Do you want to add Pepperoni? ")
    pp = input("Y/N: ")
    print("Do you want to add extra cheese? ")
    pc = input("Y/N: ")
    if pp == 'Y' and pc == 'Y':
        z = z + pl + c
        print(f"Pay ${z}")
    elif pp == 'Y' and pc == 'N':
        z = z + pl
        print(f"Pay ${z}")
    elif pp == 'N' and pc == 'Y':
        z = z + c
        print(f"Pay ${z}")
    elif pp == 'N' and pc == 'N':
        print(f"Pay ${z}") 
    else:
        print("Invalid Input")
else:
    print("Invalid input")


