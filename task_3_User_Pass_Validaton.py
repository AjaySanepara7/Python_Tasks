import re

username = input("Enter username of your choice: ")

is_username_valid = 0
conditions = [
    ("Username sholud atleast contain 8 letters",len(username) >= 8),
    ("Username sholud have atleast one '.'", "." in username),
    ("Username sholud have atleast one '_'", "_" in username),
]

for x in conditions:
    for y in x:
        if (y) == False:
            print(x[0])
            is_username_valid = 1

        
while is_username_valid == 1:

    username = input("Enter a valid username: ")
    is_username_valid = 0

    conditions = [
    ("Username sholud atleast contain 8 letters",len(username) >= 8),
    ("Username sholud have atleast one '.'", "." in username),
    ("Username sholud have atleast one '_'", "_" in username),
    ]

    for condition in conditions:
        for message in condition:
            if (message) == False:
                print(condition[0])
                is_username_valid = 1

   
password = input("Enter password: ")
is_password_valid = 0

pass_conditions = [
    ("Password should contain atleast one of these character @,#,$,%", bool(re.search("[@#$%]", password))),
    ("Password sholud have atleast one lowercase letter", bool(re.search("[a-z]", password))),
    ("Password sholud have atleast one uppercase letter", bool(re.search("[A-Z]", password))),
    ("Password should contain atleast one digit from 0-9", bool(re.search("[0-9]", password))),
]

for condition in pass_conditions:
    for message in condition:
        if message == False:
            print(condition[0])
            is_password_valid = 1


while is_password_valid == 1:

    password = input("Enter a valid password: ")
    is_password_valid = 0

    pass_conditions = [
    ("Password should contain atleast one of these character @,#,$,%", bool(re.search("[@#$%]", password))),
    ("Password sholud have atleast one lowercase letter", bool(re.search("[a-z]", password))),
    ("Password sholud have atleast one uppercase letter", bool(re.search("[A-Z]", password))),
    ("Password should contain atleast one digit from 0-9", bool(re.search("[0-9]", password))),
    ]

    for condition in pass_conditions:
        for message in condition:
            if message == False:
                print(condition[0])
                is_password_valid = 1
