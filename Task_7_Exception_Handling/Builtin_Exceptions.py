# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something went wrong")
# else:
#     print("everything in alright")
# finally:
#     print("The 'try except' is finished")


# try:
#     open("demo.txt")
# except:
#     print("Something went wrong while openin the file")


# try:
#     file_data = open("demo.txt")
#     try:
#         file_data.write("Lorem Ipsum")
#     except:
#         print("Something went wrong when writing to the file")
# except:
#     print("Something went wrong when opening the file")


# try:
#     sys.exit()
# except:
#     print("Name sys not defined, import sys first")


# try:
#     int("d")
# except:
#     print("Invalid literal for int")

# try:
#     print("d" + 1)
# except:
#     print("Can only concatenate string not string to int")

# try:
#     country = {
#         "India": "Delhi"
#     }
#     print(country["China"])
# except:
#     print("The key does not exist in the dictionary")


# try:
#     sports = ["Cricket","Football"]
#     print(sports[5])
# except:
#     print("Index does not exist")


# try:
#     pi = 2/0
# except:
#     print("ZeroDivisionError can't divide with zero")


# try:
#     def d():
#         print(f)
#         f = 2

#     d()
# except:
#     print("local variable is referenced before it is assigned")