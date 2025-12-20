# CodSoft Python Internship Task
# Task Name: To-Do List
# Author: Kaavya B M


todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "status": "Pending"})
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task['task']} - {task['status']}")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as completed: "))
        todo_list[task_no - 1]["status"] = "Completed"
        print("Task marked as completed!")
    except:
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = todo_list.pop(task_no - 1)
        print(f"Deleted task: {removed['task']}")
    except:
        print("Invalid input!")

# Main Program Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
