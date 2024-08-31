import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list."""
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        """Remove a task from the to-do list by its number."""
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")

    def display_tasks(self):
        """Display all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def clear_tasks(self):
        """Clear all tasks from the to-do list."""
        self.tasks.clear()
        print("All tasks have been cleared.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_number)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            print("Exiting the to-do list app.")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
