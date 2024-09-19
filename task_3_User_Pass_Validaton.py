import re

username = input("Enter username of your choise: ")


is_username_valid = 0

if len(username) < 8:
    print("Username sholud atleast contain 8 letters")
    is_username_valid = 1

if not re.search("\.", username):
    print("Username sholud have atleast one '.'")
    is_username_valid = 1

if not re.search("_", username):
    print("Username sholud have atleast one '_'")
    is_username_valid = 1
    
if is_username_valid == 0:
    print("Valid Username")


        
while is_username_valid == 1:

    username = input("Enter a valid username: ")
    is_username_valid = 0

    if len(username) < 8:
        print("Username sholud atleast contain 8 letters")
        is_username_valid = 1

    if not re.search("\.", username):
        print("Username sholud have atleast one '.'")
        is_username_valid = 1

    if not re.search("_", username):
        print("Username sholud have atleast one '_'")
        is_username_valid = 1



password = input("Enter password: ")

is_password_valid = 0

if not re.search("[@#$%]", password):
    print("Password should contain atleast one of these character @,#,$,%")
    is_password_valid = 1

if not re.search("[a-z]", password):
    print("Password sholud have atleast one lowercase letter")
    is_password_valid = 1

if not re.search("[A-Z]", password):
    print("Password sholud have atleast one uppercase letter")
    is_password_valid = 1

if not re.search("[0-9]", password):
    print("Password should contain atleast one digit from 0-9")
    is_password_valid = 1

if is_password_valid == 0:
    print("Valid Password")


while is_password_valid == 1:

    password = input("Enter a valid password: ")
    is_password_valid = 0

    if not re.search("[@#$%]", password):
        print("Enter atleast one of these character @,#,$,%")
        is_password_valid = 1

    if not re.search("[a-z]", password):
        print("Password sholud have atleast one lowercase letter")
        is_password_valid = 1

    if not re.search("[A-Z]", password):
        print("Password sholud have atleast one uppercase letter")
        is_password_valid = 1

    if not re.search("[0-9]", password):
        print("Password should contain atleast one digit from 0-9")
        is_password_valid = 1


      