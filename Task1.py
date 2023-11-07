class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{index + 1}. Description: {task.description}")
                print(f"   Due Date: {task.due_date}")
                print(f"   Priority: {task.priority}")
                print(f"   Status: {status}")
                print()

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description, due_date, priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = description
            task.due_date = due_date
            task.priority = priority
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            to_do_list.add_task(description, due_date, priority)
        elif choice == "2":
            to_do_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            to_do_list.mark_task_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to update: "))
            description = input("Enter updated task description: ")
            due_date = input("Enter updated due date: ")
            priority = input("Enter updated priority: ")
            to_do_list.update_task(task_index, description, due_date, priority)
        elif choice == "5":
            task_index = int(input("Enter the task index to remove: "))
            to_do_list.remove_task(task_index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
