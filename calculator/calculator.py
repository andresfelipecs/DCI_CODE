def run():

    number1 = int(input("Enter first number: "))
    operation = str(input("Enter operation: "))
    number2 = int(input("Enter second number: "))

    if operation == "+":
        result = number1 + number2

    elif operation == "-":
        result = number1 - number2

    print("The result is: ", result)


if __name__ == "__main__":
    run()
