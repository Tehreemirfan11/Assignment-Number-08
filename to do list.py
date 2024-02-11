to_do_list = []
def add_task():
    task_name = input("task name: ")
    due_date = input("due date: ")
    priority = input("priority (urgent, important, less important): ")

    if due_date < "2024-02-11" and priority == "urgent":
        category = "Urgent and Important"
    elif due_date < "2024-02-11" and priority == "important":
        category = "Important"
    elif due_date < "2024-02-11" and priority == "less important":
        category = "Less Important"
    else:
        category = "Not Scheduled"

    task = {"Task Name": task_name, "Due Date": due_date, "Priority": priority, "Category": category}
    to_do_list.append(task)
    print("Task added")

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View To-Do List")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        if not to_do_list:
            print("No tasks")
        else:
            for task in to_do_list:
                print("\nTask Name:", task["Task Name"])
                print("Due Date:", task["Due Date"])
                print("Priority:", task["Priority"])
                print("Category:", task["Category"])
    elif choice == "3":
        print("Thank You")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")