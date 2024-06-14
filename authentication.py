import os
from heading import topheading
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == "" or password == "":
            print("Username and password are required.")
            continue

        if not os.path.exists("database.txt"):
            open("database.txt", "w").close()

        with open("database.txt", "r") as f:
            for line in f:
                file_username, _ = line.strip().split(",")
                if username == file_username:
                    print("Username already exists. Please choose another username.\n")
                    break
            else:
                hashed_password = hash_password(password)

                with open("database.txt", "a") as f:
                    f.write(f"{username},{hashed_password}\n")
                topheading("User Registered")
                print("User registered successfully!")
                break

def login(username, password):

    if username == "" or password == "":
        print("Username and password are required.")
        return False

    if not os.path.exists("database.txt"):
        print("No registered users. Please sign up first.")
        return False

    hashed_password = hash_password(password)

    with open("database.txt", "r") as f:
        for line in f:
            file_username, file_password = line.strip().split(",")
            if username == file_username:
                if hashed_password == file_password:
                    print("Login successful!")
                    return True
                else:
                    print("Invalid password.")
                    return False
        print("User not found.")
        return False
