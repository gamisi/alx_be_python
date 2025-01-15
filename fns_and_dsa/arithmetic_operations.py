def perform_operation(num1,num2,operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

def main():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second nuber:"))
    operation =(input("Enter the operation ('add', 'subtract', 'multiply', or 'divide'))"))
    result = perform_operation(num1,num2,operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()