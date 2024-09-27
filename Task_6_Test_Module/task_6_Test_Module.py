import csv


input_name = input("Enter your name: ")
input_password = input("Enter your password: ")

with open("user_data.csv", "r") as userFile:
    userData = csv.DictReader(userFile)
    for lines in userData:
        while input_name != lines['username']:
            input_name = input("Enter a valid username: ")

        while input_password != lines['password']:
            input_password = input("Enter a valid password: ")

count = 0
with open("test_data.csv", "r") as testFile:
    testData = csv.reader(testFile)
    for lines in testData:
        for x in range(len(lines)-1):
            print(lines[x])
        answer = input()
        if str(answer).lower() == lines[len(lines)-1].lower():
            count += 1

print(f"The total number of correct answers are: {count}")
