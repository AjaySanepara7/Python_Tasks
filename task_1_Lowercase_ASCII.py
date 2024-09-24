name = input("Enter your name: ")

def verify_name(name):
    print('Please enter an alphabetical name')
    name = input("Enter your name: ")

    if name.isalpha() == False:
        verify_name(name)  
    else:
        return name
    
verify_name(name)
        
for z in name:
    if z.islower():
        print(f"The ASCII value of {z} is: {ord(z)}")