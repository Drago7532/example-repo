def calculation():
    result = 0
    # Input the first number of the calculation
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input the second number of the calculation
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input the operation
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid input")

    # Calculate the result
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        # Display the result
        equation = f"{num1} {operation} {num2} = {result}"
        print("Result:", result)

        # Record the calculation in the txt file
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")

    # Error handler
    except ZeroDivisionError:
        print("Cannot divide by zero")


def display_equations():
    try:
        # Read the txt file
        with open("equations.txt", "r") as file:
            contents = file.read()
            if contents:
                print("\nPrevious Calculations:")
                print(contents)
            else:
                print("\nNo calculations found.")
    except FileNotFoundError:
        print("No record found. 'equations.txt' does not exist yet")


def main():
    while True:
        # Print options for the user
        print("\nSimple Calculator")
        print("1. Perform a calculation")
        print("2. View previous calculations")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        # Call a function based on user input
        if choice == '1':
            calculation()
        elif choice == '2':
            display_equations()
        elif choice == '3':
            print("Program ended")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
