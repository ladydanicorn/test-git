def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3

print(addThree(addTwo(5))) #goes right to left

def namePrinter(first, last, middle=""):
    return f"my name's {last}, {first}, {middle} {last}."

#print(namePrinter("James", "Fred", "Bond"))

def giveMeGroceries(thing_to_add):
    grocery_list = ["grapes", "apples", "bananas"]
    grocery_list.append("spaghetti")
    return grocery_list

print(giveMeGroceries("spaghetti"))