import os
import re

# Base path to avoid repeating
base_path = "/home/user/Desktop/Python3/Python/Practice Questions/3/"

def is_strong_password(password):
    if len(password) < 7:
        return False
    if not re.search(r"[A-Z]", password):  # At least one uppercase
        return False
    if not re.search(r"[a-z]", password):  # At least one lowercase
        return False
    if not re.search(r"[0-9]", password):  # At least one digit
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # At least one symbol
        return False
    return True


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

    # Append username
    with open(os.path.join(base_path, "user_name.txt"), "a") as u_file:
        u_file.write(user_name + "\n")

    # Loop until valid password
    while True:
        password = input("Enter password: ").strip()
        if is_strong_password(password):
            break
        else:
            print("❌ Password must be at least 7 characters long and include:")
            print("   - At least one uppercase letter")
            print("   - At least one lowercase letter")
            print("   - At least one number")
            print("   - At least one special symbol (e.g. !@#$%)")

    with open(os.path.join(base_path, "password.txt"), "a") as p_file:
        p_file.write(password + "\n")

    return True  # Proceed


# Only create names if username is new and password is valid
if user_pass():
    first_last_name()
    print("✅ Account created successfully!")
