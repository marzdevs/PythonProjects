# Initialize an empty dictionary to store tasks
tasks = {}

# Function to display the to-do list
def display_tasks():
    print("To-Do List:")
    for task, (priority, due_date) in sorted(tasks.items(), key=lambda x: x[1][1]):
        print(f"Task: {task}, Priority: {priority}, Due Date: {due_date}")

# Function to add a task to the list
def add_task(task):
    priority = input("Enter the priority level from high, medium to low: ")
    due_date = input("Enter the due date (e.g., 11/22/2023): ")
    tasks[task] = (priority, due_date)
    print(f"Added task: {task}")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        del tasks[task]
        print(f"Removed task: {task}")
    else:
        print("Task not found")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
