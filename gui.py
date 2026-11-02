
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

import bst
import general_tree
import expression_tree
import graph
import topological_sort
import critical_path
import complexity_analysis
import task_storage
import project_dependencies


tasks = task_storage.load_tasks()


class ConstructionScheduler:

    def __init__(self, root):
        self.root = root
        self.root.title("Construction Project Scheduler")
        self.root.geometry("1000x650")
        self.root.minsize(800, 550)
        self.root.configure(bg="#edf2f7")

        self.create_header()
        self.create_dashboard()
        self.create_task_table()
        self.refresh_tasks()

    def create_header(self):
        header = tk.Frame(self.root, bg="#172b4d", height=100)
        header.pack(fill="x")

        tk.Label(
            header,
            text="CONSTRUCTION PROJECT SCHEDULER",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#172b4d"
        ).pack(pady=(20, 5))

        tk.Label(
            header,
            text="Project Planning and Management System",
            font=("Arial", 11),
            fg="#dce6f5",
            bg="#172b4d"
        ).pack()

    def create_dashboard(self):
        panel = tk.Frame(self.root, bg="#edf2f7")
        panel.pack(fill="x", padx=20, pady=15)

        buttons = [
            ("Add Task", self.add_task),
            ("Edit Task", self.edit_task),
            ("Delete Task", self.delete_task),
            ("Refresh", self.refresh_tasks),
            ("Deadline BST", self.show_bst),
            ("Project Hierarchy", self.show_hierarchy),
            ("Cost Calculator", self.show_cost),
            ("Dependency Graph", self.show_graph),
            ("Topological Sort", self.show_topological),
            ("Critical Path", self.show_critical_path),
            ("Complexity Analysis", self.show_complexity),
            ("Manage Dependencies", self.manage_dependencies)
        ]

        for index, (label, command) in enumerate(buttons):
            button = tk.Button(
                panel,
                text=label,
                command=command,
                bg="#ffffff",
                fg="#172b4d",
                font=("Arial", 10, "bold"),
                width=19,
                height=2,
                relief="raised",
                cursor="hand2"
            )
            button.grid(
                row=index // 4,
                column=index % 4,
                padx=5,
                pady=5,
                sticky="ew"
            )

        for column in range(4):
            panel.grid_columnconfigure(column, weight=1)

    def create_task_table(self):
        tk.Label(
            self.root,
            text="CONSTRUCTION TASK LIST",
            font=("Arial", 16, "bold"),
            bg="#edf2f7",
            fg="#172b4d"
        ).pack(pady=10)

        columns = ("number", "task", "deadline")

        self.table = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=13
        )

        self.table.heading("number", text="No.")
        self.table.heading("task", text="Task Name")
        self.table.heading("deadline", text="Deadline (Days)")

        self.table.column("number", width=70, anchor="center")
        self.table.column("task", width=400)
        self.table.column("deadline", width=180, anchor="center")

        self.table.pack(fill="both", expand=True, padx=25, pady=10)

        self.status = tk.Label(
            self.root,
            text="Ready",
            bg="#172b4d",
            fg="white",
            anchor="w",
            padx=15
        )
        self.status.pack(fill="x", side="bottom")

    def refresh_tasks(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for number, task in enumerate(tasks, start=1):
            self.table.insert(
                "",
                "end",
                values=(
                    number,
                    task["task_name"],
                    task["deadline"]
                )
            )

        self.status.config(text=f"Total Tasks: {len(tasks)}")

    def add_task(self):
        name = simpledialog.askstring(
            "Add Task",
            "Enter construction task name:",
            parent=self.root
        )

        if name is None:
            return

        name = name.strip()

        if not name:
            messagebox.showerror("Error", "Task name cannot be empty.")
            return

        if any(t["task_name"].lower() == name.lower() for t in tasks):
            messagebox.showerror("Error", "Task already exists.")
            return

        deadline = simpledialog.askinteger(
            "Add Task",
            "Enter deadline in days:",
            parent=self.root,
            minvalue=1
        )

        if deadline is None:
            return

        tasks.append({
            "task_name": name,
            "deadline": deadline
        })

        task_storage.save_tasks(tasks)
        self.refresh_tasks()
        messagebox.showinfo("Success", "Task added successfully!")

    def selected_task(self):
        selection = self.table.selection()

        if not selection:
            messagebox.showwarning(
                "Select Task",
                "Please select a task from the table."
            )
            return None

        values = self.table.item(selection[0], "values")
        return int(values[0]) - 1

    def edit_task(self):
        index = self.selected_task()

        if index is None:
            return

        task = tasks[index]

        name = simpledialog.askstring(
            "Edit Task",
            "Enter new task name:",
            initialvalue=task["task_name"],
            parent=self.root
        )

        if name is None:
            return

        name = name.strip()

        if not name:
            messagebox.showerror("Error", "Task name cannot be empty.")
            return

        if any(
            i != index and t["task_name"].lower() == name.lower()
            for i, t in enumerate(tasks)
        ):
            messagebox.showerror("Error", "Task name already exists.")
            return

        deadline = simpledialog.askinteger(
            "Edit Task",
            "Enter new deadline in days:",
            initialvalue=task["deadline"],
            minvalue=1,
            parent=self.root
        )

        if deadline is None:
            return

        old_name = task["task_name"]
        task["task_name"] = name
        task["deadline"] = deadline

        dependencies = project_dependencies.load_dependencies()

        for dependency in dependencies:
            if dependency["before"] == old_name:
                dependency["before"] = name
            if dependency["after"] == old_name:
                dependency["after"] = name

        project_dependencies.save_dependencies(dependencies)
        task_storage.save_tasks(tasks)
        self.refresh_tasks()

        messagebox.showinfo("Success", "Task updated successfully!")

    def delete_task(self):
        index = self.selected_task()

        if index is None:
            return

        if messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this task?"
        ):
            deleted = tasks.pop(index)

            dependencies = project_dependencies.load_dependencies()
            dependencies = [
                d for d in dependencies
                if d["before"] != deleted["task_name"]
                and d["after"] != deleted["task_name"]
            ]

            project_dependencies.save_dependencies(dependencies)
            task_storage.save_tasks(tasks)
            self.refresh_tasks()

            messagebox.showinfo("Success", "Task deleted successfully!")

    def show_output(self, title, function):
        try:
            import io
            from contextlib import redirect_stdout

            output = io.StringIO()

            with redirect_stdout(output):
                function()

            result = output.getvalue()

            if not result:
                result = "No output was produced."

            window = tk.Toplevel(self.root)
            window.title(title)
            window.geometry("650x450")

            text = tk.Text(
                window,
                wrap="word",
                font=("Consolas", 11),
                padx=10,
                pady=10
            )
            text.pack(fill="both", expand=True)

            text.insert("1.0", result)
            text.config(state="disabled")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def show_bst(self):
        def action():
            root = None
            for task in tasks:
                root = bst.insert(
                    root,
                    task["deadline"],
                    task["task_name"]
                )
            print("TASKS SORTED BY DEADLINE")
            bst.inorder(root)

        if not tasks:
            messagebox.showinfo("Information", "Add tasks first.")
            return

        self.show_output("Deadline Management", action)

    def show_hierarchy(self):
        self.show_output(
            "Project Hierarchy",
            general_tree.run_general_tree
        )

    def show_cost(self):
        self.show_output(
            "Construction Cost Calculator",
            expression_tree.run_expression_tree
        )

    def show_graph(self):
        self.show_output(
            "Task Dependency Graph",
            graph.run_graph
        )

    def show_topological(self):
        self.show_output(
            "Topological Sorting",
            topological_sort.run_topological_sort
        )

    def show_critical_path(self):
        self.show_output(
            "Critical Path Analysis",
            critical_path.run_critical_path
        )

    def show_complexity(self):
        self.show_output(
            "Complexity Analysis",
            complexity_analysis.run_complexity_analysis
        )

    def manage_dependencies(self):
        self.show_output(
            "Manage Dependencies",
            lambda: project_dependencies.manage_dependencies(tasks)
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = ConstructionScheduler(root)
    root.mainloop()
