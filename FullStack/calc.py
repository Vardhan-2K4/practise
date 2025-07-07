class Calculator:
    """
    A simple Calculator class that performs basic arithmetic operations.
    """

    def add(self, num1, num2):
        """
        Adds two numbers.
        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.
        Returns:
            float or int: The sum of num1 and num2.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Subtracts the second number from the first.
        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.
        Returns:
            float or int: The difference between num1 and num2.
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiplies two numbers.
        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.
        Returns:
            float or int: The product of num1 and num2.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divides the first number by the second.
        Includes error handling for division by zero.
        Args:
            num1 (float or int): The dividend.
            num2 (float or int): The divisor.
        Returns:
            float or None: The quotient of num1 and num2, or None if division by zero occurs.
        """
        try:
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return num1 / num2
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None
        except TypeError:
            print("Error: Invalid input type for division.")
            return None

def get_numbers():
    """
    Prompts the user to enter two numbers and validates the input.
    Returns:
        tuple or None: A tuple containing the two numbers (num1, num2) if valid,
                       otherwise None.
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def calculator_program():
    """
    Main function to run the calculator program.
    """
    calculator = Calculator()

    while True:
        print("\n--- Simple Calculator Menu ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        print("------------------------------")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '5':
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            numbers = get_numbers()
            if numbers is None:
                continue # Skip to next loop iteration if numbers are invalid

            num1, num2 = numbers
            result = None

            if choice == '1':
                result = calculator.add(num1, num2)
                operation_symbol = "+"
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                operation_symbol = "-"
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                operation_symbol = "*"
            elif choice == '4':
                result = calculator.divide(num1, num2)
                operation_symbol = "/"

            if result is not None: # Only print result if operation was successful (e.g., no division by zero)
                print(f"Result: {num1} {operation_symbol} {num2} = {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator_program()