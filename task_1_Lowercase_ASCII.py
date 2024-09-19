name = input("Enter your name: ")

while name.isalpha()  == False:
    print('Please enter an alphabetical name')
    name = input("Enter your name: ")  


for z in name:
    if z.islower():
        print(f"The ASCII value of {z} is: {ord(z)}")