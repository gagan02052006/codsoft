class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {deleted_task.description}")
        else:
            print("Invalid task number!")

    def update_task(self, task_number, new_description):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].description = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task number!")


def main():
    todo = ToDoList()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            num = int(input("Enter task number to mark as done: "))
            todo.mark_task_done(num)
        elif choice == '4':
            num = int(input("Enter task number to update: "))
            new_desc = input("Enter new description: ")
            todo.update_task(num, new_desc)
        elif choice == '5':
            num = int(input("Enter task number to delete: "))
            todo.delete_task(num)
        elif choice == '6':
            print("Exiting To-Do List. Have a productive day!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()