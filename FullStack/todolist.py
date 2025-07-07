TODO_FILE = "todos.txt"

def load_todos():
    """Reads and returns all to-do items from the file."""
    try:
        with open(TODO_FILE, 'r') as file:
            todos = [line.strip() for line in file if line.strip()]
        return todos
    except FileNotFoundError:
        return []
    except IOError as e:
        print(f"Error reading file: {e}")
        return []

def save_todos(todos):
    """Saves the current list of to-do items to the file."""
    try:
        with open(TODO_FILE, 'w') as file:
            for todo in todos:
                file.write(todo + '\n')
    except IOError as e:
        print(f"Error saving file: {e}")

def add_todo_item():
    """Prompts for a new to-do item, adds it, and saves the list."""
    todo_item = input("Enter a new to-do item: ").strip()
    if todo_item:
        todos = load_todos()
        todos.append(todo_item)
        save_todos(todos)
        print(f"To-do item '{todo_item}' added.")
    else:
        print("To-do item cannot be empty.")

def view_todo_items():
    """Reads and displays all to-do items from the file."""
    todos = load_todos()
    if not todos:
        print("No to-do items yet!")
        return

    print("\n--- Your To-Do List ---")
    for i, todo in enumerate(todos):
        print(f"{i + 1}. {todo}")
    print("-----------------------")

def todo_list_program():
    """Main function to run the to-do list program."""
    print("Welcome to your File-Based To-Do List!")

    while True:
        print("\n--- Menu ---")
        print("add   - Add a new to-do item")
        print("view  - View all to-do items")
        print("exit  - Exit the program")
        print("------------")

        command = input("Enter command: ").strip().lower()

        if command == 'add':
            add_todo_item()
        elif command == 'view':
            view_todo_items()
        elif command == 'exit':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid command. Please choose 'add', 'view', or 'exit'.")

if __name__ == "__main__":
    todo_list_program()