
while True:
    try:
        spam = int(input("Enter the number: "))
        if spam == 1:
            print("Hello")
        elif spam == 2:
            print("Howdy")
        else:
            print("Greetings!")
    except:
        print("Enter ineger number only")
