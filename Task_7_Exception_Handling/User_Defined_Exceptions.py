temperature = -1
if temperature < 0:
    raise Exception("Sorry,no numbers below zero")


age = "hello"
if not type(age) is int:
    raise TypeError("Only integers are allowed")


numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    while num < 3:
        raise Exception("Something went wrong")


country = {
    "India": "Delhi",
    "China": "Beijing"
}
if country["China"]:
    raise Exception("Invalid country name")