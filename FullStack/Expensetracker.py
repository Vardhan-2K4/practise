def add_expense(expenses):
    """Adds a new expense to the expense list."""
    description = input("Enter expense description: ").strip()
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be a positive number. Please try again.")
            else:
                expenses.append((description, amount))
                print(f"Expense '{description}' (₹{amount:.2f}) added successfully!")
                break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def view_expenses(expenses):
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses to display.")
        return

    print("\n--- All Expenses ---")
    for i, (description, amount) in enumerate(expenses):
        print(f"{i + 1}. Description: {description}, Amount: ₹{amount:.2f}")
    print("--------------------")

def calculate_total_expenses(expenses):
    """Calculates and displays the total of all expenses."""
    if not expenses:
        print("No expenses to calculate total for.")
        return

    total = sum(amount for description, amount in expenses)
    print(f"\n--- Total Expenses ---")
    print(f"Total amount spent: ₹{total:.2f}")
    print("----------------------")

def expense_tracker_program():
    """Main function to run the expense tracker program."""
    expenses = []

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")
        print("----------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total_expenses(expenses)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    expense_tracker_program()