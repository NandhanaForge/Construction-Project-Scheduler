# 🏗️ Construction Project Scheduler

A Python-based Construction Project Scheduler developed using **Data Structures and Algorithms (DSA)**. The application helps manage construction tasks, organize project activities, and analyze task dependencies through a simple Tkinter graphical user interface.

## 📌 Project Overview

The Construction Project Scheduler is designed to make construction task management easier. It provides features to add, edit, delete, and display tasks while demonstrating important data structures and algorithms.

The project also includes task dependency management, deadline-based organization, and construction cost calculation.

## ✨ Features

- **Task Management:** Add, view, edit, and delete construction tasks.
- **Deadline Organization:** Organize tasks using a Binary Search Tree (BST).
- **Project Hierarchy:** Represent project structure using a General Tree.
- **Cost Calculation:** Evaluate construction cost expressions using an Expression Tree.
- **Task Dependencies:** Represent dependencies between tasks using a Graph.
- **Cycle Detection:** Detect dependency cycles using Depth-First Search (DFS).
- **Topological Sorting:** Determine a valid order for dependent tasks.
- **Critical Path Analysis:** Demonstrate critical path calculations using sample project data.
- **Data Persistence:** Store task and dependency information using JSON files.
- **Graphical User Interface:** Interact with the application through Tkinter.

## 🧠 Data Structures and Algorithms Used

| Concept | Application |
|---|---|
| Binary Search Tree (BST) | Organizing tasks by deadline |
| General Tree | Representing project hierarchy |
| Expression Tree | Construction cost expression evaluation |
| Graph | Representing task dependencies |
| Depth-First Search (DFS) | Detecting dependency cycles |
| Topological Sorting | Finding a valid task execution order |
| Critical Path Analysis | Demonstrating project scheduling analysis |
| JSON | Saving task and dependency data |

## 🛠️ Technologies Used

- Python 3
- Tkinter
- JSON
- Visual Studio Code
- Git and GitHub

## 📂 Project Structure

```text
Construction_Project_Scheduler/
│
├── main.py
├── gui.py
├── bst.py
├── general_tree.py
├── expression_tree.py
├── graph.py
├── topological_sort.py
├── critical_path.py
├── complexity_analysis.py
├── task_storage.py
├── project_dependencies.py
├── README.md
├── .gitignore
│
└── screenshots/
    └── gui.png
```

The `tasks.json` and `dependencies.json` files are generated locally when the application stores data.

## ▶️ How to Run the Project

### Requirements

- Python 3 installed on your computer.
- Tkinter available with your Python installation.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/NandhanaForge/Construction-Project-Scheduler.git
```

2. Open the project folder:

```bash
cd Construction-Project-Scheduler
```

3. Run the graphical application:

```bash
python gui.py
```

4. The Construction Project Scheduler GUI will open.

## 📸 Application Screenshots

### Main GUI

![Construction Project Scheduler GUI](screenshots/gui.png)

## 🎯 Learning Outcomes

- Understanding and implementing different data structures.
- Applying graph algorithms to project dependencies.
- Using trees for task organization and cost evaluation.
- Understanding scheduling and critical path concepts.
- Building a desktop application using Python Tkinter.
- Saving and retrieving application data using JSON.



---

⭐ If you find this project useful, feel free to explore the code and learn from it!
