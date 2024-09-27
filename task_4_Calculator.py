class Calculator:
    def __init__(self, a):
        self.a = a

    def add(self, operand2):
        return self.a + operand2.a

    def subtract(self, operand2):
        return self.a - operand2.a

    def multiply(self, operand2):
        return self.a * operand2.a

    def divide(self, operand2):
        return self.a / operand2.a

    def power(self, operand2):
        return self.a**operand2.a

    def remainder(self, operand2):
        return self.a % operand2.a

    def bitwise_left_shift(self, operand2):
        return self.a << operand2.a

    def bitwise_right_shift(self, operand2):
        return self.a >> operand2.a

    def bitwise_and(self, operand2):
        return self.a & operand2.a

    def bitwise_or(self, operand2):
        return self.a | operand2.a

    def bitwise_xor(self, operand2):
        return self.a ^ operand2.a

    def bitwise_not(self, operand2):
        return ~self.a

    def less_than(self, operand2):
        return self.a < operand2.a

    def less_than_equalto(self, operand2):
        return self.a <= operand2.a

    def equalto(self, operand2):
        return self.a == operand2.a

    def not_equalto(self, operand2):
        return self.a != operand2.a

    def greater_than(self, operand2):
        return self.a > operand2.a

    def greater_than_equalto(self, operand2):
        return self.a >= operand2.a


choice = 1
while choice != 0:

    input_1 = int(input("Enter the first number: "))
    input_2 = int(input("Enter the second number: "))

    operand1 = Calculator(input_1)

    operand2 = Calculator(input_2)

    print(
        "0. Exit\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Power\n"
        "6. Remainder\n"
        "7. Bitwise Left Shift\n"
        "8. Bitwise Right Shift\n"
        "9. Bitwise AND\n"
        "10. Bitwise OR\n"
        "11. Bitwise XOR\n"
        "12. Bitwise NOT\n"
        "13. Less than\n"
        "14. Less than or equal to\n"
        "15. Equal to\n"
        "16. Not equal to\n"
        "17. Greater than\n"
        "18. Greater than or equal to\n"
    )

    choice = int(input("Enter your choice: "))
    print()

    result1 = lambda choice: print(
        "The computed addition result is : ", operand1.add(operand2), "\n"
    )
    result2 = lambda choice: print(
        "The computed subtraction result is : ", operand1.subtract(operand2)
    )
    result3 = lambda choice: print(
        "The computed multiplication result is : ", operand1.multiply(operand2)
    )
    result4 = lambda choice: print(
        "The computed division result is : ", operand1.divide(operand2)
    )
    result5 = lambda choice: print(
        "The computed exponentiation result is : ", operand1.power(operand2)
    )
    result6 = lambda choice: print(
        "The computed remainder result is : ", operand1.remainder(operand2)
    )
    result7 = lambda choice: print(
        "The computed bitwise left shift result is : ",
        operand1.bitwise_left_shift(operand2),
    )
    result8 = lambda choice: print(
        "The computed bitwise right shift result is : ",
        operand1.bitwise_right_shift(operand2),
    )
    result9 = lambda choice: print(
        "The computed bitwise and result is : ", operand1.bitwise_and(operand2)
    )
    result10 = lambda choice: print(
        "The computed bitwise or result is : ", operand1.bitwise_or(operand2)
    )
    result11 = lambda choice: print(
        "The computed bitwise xor result is : ", operand1.bitwise_xor(operand2)
    )
    result12 = lambda choice: print(
        "The computed bitwise not result is : ", operand1.bitwise_not(operand2)
    )
    result13 = lambda choice: print(
        "The computed less than result is : ", operand1.less_than(operand2)
    )
    result14 = lambda choice: print(
        "The computed less than equal to result is : ",
        operand1.less_than_equalto(operand2),
    )
    result15 = lambda choice: print(
        "The computed equal to result is : ", operand1.equalto(operand2)
    )
    result16 = lambda choice: print(
        "The computed not equal to result is : ", operand1.not_equalto(operand2)
    )
    result17 = lambda choice: print(
        "The computed greater than result is : ", operand1.greater_than(operand2)
    )
    result18 = lambda choice: print(
        "The computed greater than equal to result is : ",
        operand1.greater_than_equalto(operand2),
    )
    result0 = lambda choice: print("Exit")
    result20 = lambda choice: print("Sorry, invalid choice")

    choice_list = [
        result0,
        result1,
        result2,
        result3,
        result4,
        result5,
        result6,
        result7,
        result8,
        result9,
        result10,
        result11,
        result12,
        result13,
        result14,
        result15,
        result16,
        result17,
        result18,
        result20,
    ]

    if choice > 18:
        choice_list[len(choice_list) - 1](choice)
    else:
        choice_list[choice](choice)
