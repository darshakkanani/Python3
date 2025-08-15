# Login Page

while True:
    try:
        user_name = input("Enter your usename: ")
        with open("/home/user/Desktop/Python/Practice Questions/2/user_name.txt","r") as user_file:
            usernames = [line.strip() for line in user_file]
            if user_name != user_name:
                print("Try again ! Enter right username")
            else:
                index0 = usernames.index(user_name)
                user_password = input("Enter password: ")
                with open("/home/user/Desktop/Python/Practice Questions/2/user_password.txt","r") as pass_file:
                    passwords = [line.strip() for line in pass_file]
                    index1 = passwords.index(user_password)
                    if passwords[index0] != passwords[index1]:
                        print("Try again! Enter the correct Password")
                    else:
                        print("Access granted!")
                        break
    except:
        print("Enter right username and paswword")