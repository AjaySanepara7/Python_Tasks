name = input("Enter your name: ")

def verify_name(name):
    if name.isalpha() == False:
        print('Please enter an alphabetical name')
        name = input("Enter your name: ")
        return verify_name(name)  
    else:
        return name

    
name = verify_name(name)
        
for z in name:
    if z.islower():
        print(f"{z} : {ord(z)}")