from todo_operations import add_task, view_tasks, delete_task
from utils import clear_screen, read_input

def main():
    tasks = []

    while True:
        clear_screen()
        print("To-Do List Application")
        print("1. Add a new to-do item")
        print("2. View all to-do items")
        print("3. Delete a to-do item")
        print("4. Exit")

        choice = read_input("Choose an option (1-4): ")

        if choice == '1':
            task = read_input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            index = int(read_input("Enter the index of the task to delete: "))
            delete_task(tasks, index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        read_input("Press Enter to continue...")

if __name__ == "__main__":
    main()
