class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))

myObject = Calculator(input_1, input_2)

choise = 1
while choise != 0:
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")

    choise = int(input("Enter your choise: "))

    if choise == 1:
        print("The computed addition result is : ", myObject.add())
    elif choise == 2:
        print("The computed subtraction result is : ", myObject.subtract())
    elif choise == 3:
        print("The computed multiplication result is : ", myObject.multiply())
    elif choise == 4:
        print("The computed division result is : ", myObject.divide())
    elif choise == 0:
        print("Exit")
    else:
        print("Sorry, invalid choise!")
print()