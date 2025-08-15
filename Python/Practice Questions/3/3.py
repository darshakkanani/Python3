import os

# Base path to avoid repeating
base_path = "/home/user/Desktop/Python3/Python/Practice Questions/3/"

def first_last_name():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    with open(os.path.join(base_path, "first_name.txt"), "a") as f_file:
        f_file.write(first_name + "\n")

    with open(os.path.join(base_path, "last_name.txt"), "a") as l_file:
        l_file.write(last_name + "\n")


def user_pass():
    user_name = input("Enter username: ").strip()

    try:
        with open(os.path.join(base_path, "user_name.txt"), "r") as u_file:
            usernames = [line.strip() for line in u_file]
    except FileNotFoundError:
        usernames = []

    if user_name in usernames:
        print("Username already exists")
        return False  # Don't proceed
    else:
        with open(os.path.join(base_path, "user_name.txt"), "a") as u_file:
            u_file.write(user_name + "\n")

        password = input("Enter password: ").strip()
        with open(os.path.join(base_path, "password.txt"), "a") as p_file:
            p_file.write(password + "\n")

        return True  # Proceed


# Only create names if username is new
if user_pass():
    first_last_name()
    print("Account created successfully!")
