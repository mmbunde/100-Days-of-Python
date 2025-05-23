def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero!"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("Welcome to the Python Calculator!")
    should_continue = True

    while should_continue:
        num1 = float(input("Enter the first number: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Choose an operation: ")
        num2 = float(input("Enter the second number: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input("Type 'yes' to continue, or 'no' to exit: ").lower() != "yes":
            should_continue = False
            print("Goodbye!")

calculator()
