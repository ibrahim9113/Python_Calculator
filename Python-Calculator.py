def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        result = num1 / num2
    else:
        return "Invalid operator!"

    return f"Result: {result}"

# Run the calculator
print(calculator())
