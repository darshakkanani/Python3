print("Welcome to Treasure Island. Your mission is to find the treasure.")

a = input("Choose your path (LEFT/RIGHT): ")
b = a.lower()

if b == 'left':
    c = input("Choose your path (WAIT/RUN): ")
    d = c.lower()
    if d == 'wait':
        e = input("Which door (RED/YELLO/BLUE): ")
        f = e.lower()
        if f == 'yellow':
            print("You Win!")
        elif f == 'blur' or f == 'red':
            print("Game Over")
        else:
            print("Invalid input")
    elif d == 'run':
        print("Game Over")
    else:
        print("Invalid input")
elif b == 'right':
    print("Game Over")
else:
    print("Invalid input")
