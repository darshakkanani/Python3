count = 1
while count == 1:
    temp = input("Please Enter a number btw 1-9: ")
    try:
        number = int(temp)
    except:
        print("Please enter a interger only")
    else:
        if int(temp) < 1 or int(temp) > 9:
            print("Please enter number btw 1 - 9")
        else: 
            count = 0
# option = 1
while True:
    print("1. Enter")
    print("2. Exit")
    option = input("Enter your choice: ")
    try:
        if int(option) == 1:
            if number <= 2:
                print("You can walk")
            elif number >= 2 and number <= 5:
                print("You can run")
            else:
                print("You can do anything")
        elif int(option) == 2:
            print("Exiting....")
            break
        else:
            print("Enter 1 or 2")
    except:
        input("Please Enter an integer only: ")

 
