
import json
import os

FILE_NAME = "dependencies.json"


def load_dependencies():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not load dependencies.")
        return []


def save_dependencies(dependencies):
    with open(FILE_NAME, "w") as file:
        json.dump(dependencies, file, indent=4)


def manage_dependencies(tasks):
    if len(tasks) < 2:
        print("Add at least two tasks before creating dependencies.")
        return

    dependencies = load_dependencies()

    while True:
        print("\n===== TASK DEPENDENCIES =====")
        print("1. Add Dependency")
        print("2. Display Dependencies")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\nAvailable Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task_name']}")

            try:
                first = int(input("Enter prerequisite task number: "))
                second = int(input("Enter dependent task number: "))

                if not (1 <= first <= len(tasks) and
                        1 <= second <= len(tasks)):
                    print("Invalid task number.")
                    continue

                if first == second:
                    print("A task cannot depend on itself.")
                    continue

                dependency = {
                    "before": tasks[first - 1]["task_name"],
                    "after": tasks[second - 1]["task_name"]
                }

                if dependency in dependencies:
                    print("This dependency already exists.")
                    continue

                dependencies.append(dependency)
                save_dependencies(dependencies)

                print("Dependency saved successfully!")

            except ValueError:
                print("Please enter valid task numbers.")

        elif choice == "2":
            print("\nSaved Dependencies:")

            if not dependencies:
                print("No dependencies available.")
            else:
                for item in dependencies:
                    print(item["before"], "->", item["after"])

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


def run_saved_graph(tasks):
    dependencies = load_dependencies()

    if not tasks:
        print("No tasks available. Add tasks first.")
        return

    print("\n===== SAVED TASK DEPENDENCY GRAPH =====")

    for task in tasks:
        print(task["task_name"], "->", end=" ")

        connected = [
            item["after"] for item in dependencies
            if item["before"] == task["task_name"]
        ]

        print(", ".join(connected) if connected else "No dependent tasks")

    # Detect cycles using DFS
    graph = {task["task_name"]: [] for task in tasks}

    for item in dependencies:
        if item["before"] in graph and item["after"] in graph:
            graph[item["before"]].append(item["after"])

    visiting = set()
    visited = set()

    def has_cycle(node):
        if node in visiting:
            return True

        if node in visited:
            return False

        visiting.add(node)

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        visiting.remove(node)
        visited.add(node)
        return False

    cycle_found = any(
        has_cycle(node) for node in graph
        if node not in visited
    )

    if cycle_found:
        print("\nWarning: A dependency cycle was detected!")
    else:
        print("\nNo dependency cycle detected.")
