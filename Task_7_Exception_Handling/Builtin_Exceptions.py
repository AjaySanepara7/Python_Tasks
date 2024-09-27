try:
    print(x)
except NameError:
    print("1. Variable x is not defined")
except:
    print("Something went wrong")
else:
    print("everything in alright")
finally:
    print("The 'try except' is finished")


try:
    open("demo.txt./jnk")
except:
    print("2. Something went wrong while openin the file")


try:
    file_data = open("demo.txt")
    try:
        file_data.write("Lorem Ipsum")
    except:
        print("3. Something went wrong when writing to the file")
except:
    print("Something went wrong when opening the file")


try:
    sys.exit()
except:
    print("4. Name sys not defined, import sys first")


try:
    int("d")
except:
    print("5. Invalid literal for int")

try:
    print("d" + 1)
except:
    print("6. Can only concatenate string not string to int")

try:
    country = {
        "India": "Delhi"
    }
    print(country["China"])
except:
    print("7. The key does not exist in the dictionary")


try:
    sports = ["Cricket","Football"]
    print(sports[5])
except:
    print("8. Index does not exist")


try:
    pi = 2/0
except:
    print("9. ZeroDivisionError can't divide with zero")


try:
    def d():
        print(f)
        f = 2

    d()
except:
    print("10. local variable is referenced before it is assigned")