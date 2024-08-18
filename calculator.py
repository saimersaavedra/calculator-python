# Print a welcome message for the calculator
print("Welcome to the calculator", "\nTo exit, type 'Exit'",
      "\nThe available operations are add, multiply, divide, and subtract")

result = ""
while True:
    # Check if 'result' is empty
    if not result:
        result = input("Enter a number: ")
        if result.lower() == "exit":  # Exit condition
            break
        result = int(result)
    
    # Prompt for the operation
    op = input("Enter an operation: ")
    if op.lower() == "exit":  # Exit condition
        break
    
    # Prompt for the next number
    n2 = input("Enter the next number: ")
    if n2.lower() == "exit":  # Exit condition
        break
    n2 = int(n2)

    # Perform the chosen operation
    if op.lower() == "add":
        result += n2
    elif op.lower() == "subtract":
        result -= n2
    elif op.lower() == "multiply":
        result *= n2
    elif op.lower() == "divide":
        result /= n2
    else: 
        print("Invalid operation")  # Handle invalid operations
        break
    
    # Display the result of the operation
    print(f"The result is: {result}")