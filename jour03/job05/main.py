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
            return num1 / num2
        case "%":
            return num1 % num2

print(calcule(2, "*", 4))
print(calcule(5, "%", 4))
print(calcule(19, "-", 4))
