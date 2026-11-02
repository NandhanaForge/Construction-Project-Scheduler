
import bst
import general_tree
import expression_tree
import graph
import topological_sort
import critical_path
import complexity_analysis
import task_storage


# Load saved tasks
tasks = task_storage.load_tasks()


def display_menu():
    print("\n====================================")
    print(" CONSTRUCTION PROJECT SCHEDULER")
    print("====================================")
    print("1. Task Management")
    print("2. Deadline Management (BST)")
    print("3. Project Hierarchy (General Tree)")
    print("4. Construction Cost Calculator")
    print("5. Task Dependency Graph")
    print("6. Topological Sorting")
    print("7. Critical Path Analysis")
    print("8. Complexity Analysis")
    print("9. Exit")
    print("====================================")


def add_task():
    task_name = input("Enter task name: ").strip()

    if not task_name:
        print("Error: Task name cannot be empty.")
        return

    try:
        deadline = int(input("Enter deadline in days: "))

        if deadline <= 0:
            print("Error: Deadline must be greater than zero.")
            return

    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    tasks.append({
        "task_name": task_name,
        "deadline": deadline
    })

    task_storage.save_tasks(tasks)
    print("Task added successfully!")


def display_tasks():
    print("\n===== CONSTRUCTION TASKS =====")

    if not tasks:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        print(
            number, ".",
            task["task_name"],
            "- Deadline:",
            task["deadline"],
            "days"
        )


def delete_task():
    display_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return

        deleted_task = tasks.pop(task_number - 1)

        task_storage.save_tasks(tasks)

        print("Task deleted successfully:", deleted_task["task_name"])

    except ValueError:
        print("Error: Please enter a valid task number.")


def edit_task():
    display_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to edit: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return

        task = tasks[task_number - 1]

        print("\nCurrent Task:", task["task_name"])
        print("Current Deadline:", task["deadline"], "days")

        new_name = input(
            "Enter new task name (Enter to keep current): "
        ).strip()

        new_deadline = input(
            "Enter new deadline (Enter to keep current): "
        ).strip()

        # Validate the new deadline before changing either field
        if new_deadline:
            deadline = int(new_deadline)

            if deadline <= 0:
                print("Error: Deadline must be greater than zero.")
                return
        else:
            deadline = task["deadline"]

        if new_name:
            task["task_name"] = new_name

        task["deadline"] = deadline

        task_storage.save_tasks(tasks)

        print("Task updated successfully!")

    except ValueError:
        print("Error: Please enter a valid whole number for the deadline.")


def task_management():
    while True:
        print("\n===== TASK MANAGEMENT =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            edit_task()

        elif choice == "5":
            break

        else:
            print("Invalid choice! Enter 1 to 5.")


def deadline_management():
    if not tasks:
        print("\nNo tasks available. Add tasks first.")
        return

    root = None

    for task in tasks:
        root = bst.insert(
            root,
            task["deadline"],
            task["task_name"]
        )

    print("\n===== TASKS SORTED BY DEADLINE =====\n")
    bst.inorder(root)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            task_management()

        elif choice == "2":
            deadline_management()

        elif choice == "3":
            general_tree.run_general_tree()

        elif choice == "4":
            expression_tree.run_expression_tree()

        elif choice == "5":
            graph.run_graph()

        elif choice == "6":
            topological_sort.run_topological_sort()

        elif choice == "7":
            critical_path.run_critical_path()

        elif choice == "8":
            complexity_analysis.run_complexity_analysis()

        elif choice == "9":
            print("\nThank you for using Construction Project Scheduler!")
            break

        else:
            print("Invalid choice! Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
