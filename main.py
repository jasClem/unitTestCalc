import calculator

def main():

    calc = calculator.Calculator()
    firstNumber = input("\nFirst number: ")
    operation = input("\nOperation (+, -, *, /): ")
    secondNumber = input("\nSecond number: ")

    if operation == "+":
        print("\nYour answer is: " + calc.add(firstNumber, secondNumber))
    if operation == "-":
        print("\nYour answer is: " + calc.subtract(firstNumber, secondNumber))
    if operation == "*":
        print("\nYour answer is: " + calc.multiply(firstNumber, secondNumber))
    if operation == "/":
        print("\nYour answer is: " + calc.divide(firstNumber, secondNumber))
    else:
        print("\nYour operation is invalid, please try again")

main()
