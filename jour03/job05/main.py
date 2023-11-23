#Here using match case (equivalent to switch case in other languages), implemented in python 3.10
#May not work if your Python is not up to date
def calcule(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            #Using any() function that returns a boolean if any condition in the list is matched
            if any([num1 == 0, num2 == 0]):
                #Raising a ValueError that terminates the program, we could also use a simple "return"
                raise ValueError("Can't divide by 0")
            return num1 / num2
        case "%":
            return num1 % num2

print(calcule(2, "*", 4))
print(calcule(5, "%", 4))
print(calcule(19, "-", 4))
print(calcule(19, "/", 2))
print(calcule(19, "/", 0))