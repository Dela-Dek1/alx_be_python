def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
        print(f"Result: {result}")
        return result
    elif operation == "subtract":
        result = num1 + num2
        print(f"Result: {result}")
        return result
    elif operation == "multiply":
        result = num1 + num2
        print(f"Result: {result}")
        return result
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowe."
        else:
            result = num1 / num2
        print(f"Result: {result}")
        return result
    else:
        return "Try again!"

print("Arithmetic Operation")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")

result = perform_operation(num1, num2, operation)
print(f"Result: {result}")


