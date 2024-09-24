phoneDirectory = {}
namelist = []
numberlist = []

name = input("Enter name: ")
number = int(input("Enter number: "))

choice = input("Press 1 to enter another name & number \nPress any other key to exit: ")

namelist.append(f"{name}")
numberlist.append(f"{number}")

while choice == "1":
    name = input("Enter name: ")
    number = int(input("Enter number: "))
    choice = input("Press 1 to enter another name & number \nPress 0 to exit: ")
    namelist.append(f"{name}")
    numberlist.append(f"{number}")

for k,v in zip(namelist, numberlist):
    phoneDirectory.update({k: v})


operation_choice = int(input("Press 1 to search contact \nPress 2 to update contact \nPress 0 to exit: "))

while operation_choice == 1 or operation_choice == 2:
    if operation_choice == 1:
        searchInput = input("Enter name or number to search contact: ")
        for x,y in phoneDirectory.items():
            if searchInput == f"{x}" or searchInput == f"{y}":
                print(x + ": " + y)
        operation_choice = int(input("Press 1 to search contact \nPress 2 to update contact \nPress 0 to exit: "))
    elif operation_choice == 2:
        updateInput = input("Enter name or number where you want to update the contact: ")
        for x,y in list(phoneDirectory.items()):
            if updateInput == f"{x}" or updateInput == f"{y}":
                del phoneDirectory[f"{x}"]
        updatedName = input("Enter the updated name: ")
        updatedNumber = input("Enter the updated number: ")
        phoneDirectory.update({updatedName: updatedNumber})
        operation_choice = int(input("Press 1 to search contact \nPress 2 to update contact \nPress 0 to exit: "))

print(phoneDirectory)
